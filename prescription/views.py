from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from .models import Prescription,Item
from .models import Medicine
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import View
from .forms import Make_Prescription,ItemForm
from django.views import generic
from django.db.models import Max
from dal import autocomplete
from .utils import render_to_pdf
from django.template.loader import get_template
from io import BytesIO
from django.core.files import File
from doctor_profile.models import Profile
from django.views.generic import FormView, CreateView
from booking.models import AppointmentDetials
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

# Create your views here.
from django.contrib.auth.models import User
def index(request):
    return render(request,'prescription_home.html')


class DetailView(generic.DetailView):
    model=Prescription
    template_name='detail.html'


class PrescriptionCreate(CreateView):


    model=Prescription
    fields=['prescription_id',]
#################################TO PASS INITIAL VALUES ############
    def get_initial(self):
        #appointment_id=appointment_id
        max_id=Prescription.objects.all().aggregate(Max('prescription_id'))
        if list(max_id.values())[0] == None:
            value=0
        else:
            value=int(list(max_id.values())[0])
        value=value+1
        #user = request.user


        #print(value)
        #appointment_id=self.kwargs['appointment_id']
        initial = super(PrescriptionCreate, self).get_initial()
        initial.update({'prescription_id': value})
        return initial

    def get_context_data(self, **kwargs):
        context = super(PrescriptionCreate, self).get_context_data(**kwargs)
        user=self.request.user
        profile = Profile.objects.get(user=user)
        #appointment_id=int(self.kwargs['appointment_id'])
        appointment = AppointmentDetials.objects.get(pk=self.kwargs['appointment_id'])
        context['appointment']=appointment
        context['doctor']=profile
        return context



    def form_valid(self, form):
        #event = Event.objects.get(pk=self.kwargs['appointment_id'])
        user=self.request.user
        profile = Profile.objects.get(user=user)
        #appointment_id=int(self.kwargs['appointment_id'])

        #print('**')
        prescription = form.save(commit=False)

        prescription.doctor = profile
        prescription=form.save()
        appointment = AppointmentDetials.objects.get(pk=self.kwargs['appointment_id'])
        appointment.is_attended=True
        appointment.prescription=prescription
        appointment.save()
        return super(PrescriptionCreate, self).form_valid(form)

@login_required(login_url=reverse_lazy('login'))
def detail(request, pk):
    prescription = get_object_or_404(Prescription, pk=pk)
    return render(request, 'prescription/detail.html', {'prescription':prescription,'prescription_id':pk})

@login_required(login_url=reverse_lazy('login'))
def create_item(request, prescription_id):
    form = ItemForm(request.POST or None, request.FILES or None , initial={'prescription':prescription_id})
    prescription = get_object_or_404(Prescription, pk=prescription_id)
    if form.is_valid():
        prescription_items = prescription.item_set.all()
        for s in prescription_items:
            if s.medicine_name == form.cleaned_data.get("name"):
                context = {
                    'prescription': prescription,
                    'form': form,
                    #'error_message': 'You already added that medicine',
                }
                return render(request, 'prescription/create_item.html', context)
        item = form.save(commit=False)
        item.prescription = prescription
        item.save()
        return render(request, 'detail.html', {'prescription': prescription})
    context = {
        'prescription': prescription,
        'form': form,
    }
    return render(request, 'prescription/create_item.html', context)


class MedicineAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Medicine.objects.all()

        if self.q:
            qs = qs.filter(name__istartswith=self.q)
        #print(qs)
        return qs


def print(request,prescription_id):
    prescription = get_object_or_404(Prescription, pk=prescription_id)
    prescription_no=int(prescription_id)
    prescription_no=prescription_no-54

    template=get_template('prescription/print.html')
    context={"prescription_id":str(prescription_no),"prescription":prescription}
    html=template.render(context)
    pdf=render_to_pdf('prescription/print.html',context)
    filename ="prescription{}.pdf".format(prescription_id)

    if pdf:
        prescription.pdf.save(filename,File(BytesIO(pdf.content)))
        return HttpResponse(pdf,content_type='application/pdf')

    return HttpResponse('NOT FOUND')
