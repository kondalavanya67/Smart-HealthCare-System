from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from .models import Profile,BookingDate,Slot
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import Add_Profile,Modify_Profile,SlotForm
import datetime
from django.urls import reverse,reverse_lazy
from django.db.models import Max
from myapp.models import Post
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.utils.decorators import method_decorator
# Create your views here.

def index(request):

    #print(user)

    return render(request,'profile_home.html')

@login_required(login_url=reverse_lazy('login'))
def make_profile(request):
    user = request.user
    if request.method=="POST":
        form=Add_Profile(request.POST, request.FILES ,initial={'user':user,'email_id':user.email})

        if form.is_valid():
            profile_item=form.save(commit=False)
            profile_item.user = user
            profile_item.save()

            return redirect('/doctor_home/')

    else:

        form=Add_Profile(initial={'user':user,'email_id':user.email})
        #form.fields['user'].widget.attrs['disabled'] = True
        #form.fields['user'].editable=False
    return render(request,'new.html',{'form':form})


@login_required(login_url=reverse_lazy('login'))
def create_slot(request, pk):
    user=request.user
    form = SlotForm(request.POST or None, initial={'date':pk})
    date = get_object_or_404(BookingDate, pk=pk)
    if form.is_valid():

        item = form.save(commit=False)
        item.date = date
        profile = Profile.objects.get(user=user)
        item.doctor=profile
        try:
            item.save()
        except IntegrityError as e:
            context = {
                'date': date,
                'form': form,
                'message':"Slot already Exists"
            }
            return render(request, 'doctor_profile/create_slot.html', context)

        return redirect('/doctor_home/')
    context = {
        'date': date,
        'form': form,
    }

    return render(request, 'doctor_profile/create_slot.html', context)

@method_decorator(login_url=reverse_lazy('login'))
class DateCreate(CreateView):

    model=BookingDate
    fields=['date',]

    def get_initial(self):

         max_date=BookingDate.objects.all().aggregate(Max('date'))
         key, value = max_date.popitem()
         value += datetime.timedelta(days=1)
         print(value)
        # value=int(list(max_id.values())[0])
        # value=value+1
        # #user = request.user
        #
        #
        # #print(value)
         initial = super(DateCreate, self).get_initial()
         initial.update({'date': value})
         return initial
    def form_valid(self, form):
        user=self.request.user

        profile = Profile.objects.get(user=user)
        date = form.save(commit=False)
        print(date)
        try:
            obj = BookingDate.objects.filter(date=str(date)).filter(doctor=profile).first()
        except BookingDate.DoesNotExist:
            obj = None
        # obj=get_object_or_404(BookingDate, date=str(date))
        print('SHIVAM')
        print(obj)
        #print(obj.pk)
        if(obj==None):
            print("no")
            date.doctor = profile
            return super(DateCreate, self).form_valid(form)
        else:
            print('Yes')
            #return create_slot(self.request,pk=obj.pk-1)
            return redirect(str(obj.pk) + '/slot/')
            #return reverse('doctor_profile:create_slot',kwargs={'pk':int(obj.pk)})
            #return HttpResponse('OK')
            #return super(DateCreate, self).form_invalid(form)
        # context={
        #
		#     "object":appointment,
		# }
		# return render(self.request,'booking/booking_confirmation.html', context=context)

@login_required(login_url=reverse_lazy('login'))
def date_create(request):
    user=request.user
    profile=Profile.objects.get(user=user)

    date=BookingDate.objects.create(doctor=profile,date=datetime.now())

    return HttpResponse('Done')

@login_required(login_url=reverse_lazy('login'))
def modify_profile(request):
    user = request.user
    profile_item = Profile.objects.get(user=user)
    form=Modify_Profile(request.POST or None, instance=profile_item)
    if form.is_valid():
            form.save()
            return redirect('/doctor_home/')
    return render(request,'new.html',{'form':form})

@login_required(login_url=reverse_lazy('login'))
def Show_Profile(request):
        user = request.user
        profile = Profile.objects.get(user=user)
        context={
            'profile':profile
        }
        return render(request,'show_profile.html',context)
