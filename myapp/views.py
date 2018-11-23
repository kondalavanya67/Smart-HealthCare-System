from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Post, Rmplist
from doctor_profile.models import Profile
from rmp.models import rmpContact
# Create your views here.


def index(request):
    if(request.method=="POST"):
        name=request.POST['doctor']
        u=Post.objects.get(doctor_name=Profile.objects.get(first_name=name))
        x=u.doctor_name.gender
        y=u.doctor_name.last_name
        z=u.doctor_name.email_id
        v=u.doctor_name.speciality
        l=u.doctor_name.qualification
        j=u.doctor_name.mobile_no
        k=u.doctor_name.locality
        o=u.doctor_name.hospital
        return HttpResponse('Gender:' + x + '<br>' + 'Last_name:' + y + '<br>' + 'Email_id:' + z + '<br>' + 'Speciality:' + v + '<br>' + 'Qualification:'+ l +'<br>'+'Locality:'+ k +'<br>'+ 'Hospital:' + o + '<br>'+'<input type="button" value="Accept">' + '<input type="button" value="Reject">')
    else:
        all_data = Post.objects.all()

        return render(request, 'myapp/index.html', {'all_data':all_data})


def rmpdetails(request):
    if(request.method=="POST"):
        name=request.POST['rmp']
        u=Rmplist.objects.get(rmp_list=rmpContact.objects.get(first_name=name))
        x=u.rmp_list.gender
        y=u.rmp_list.last_name
        z=u.rmp_list.email_id
        #v=u.rmp_list.speciality
        l=u.rmp_list.qualification
        j=u.rmp_list.mobile_no
        k=u.rmp_list.locality
        o=u.rmp_list.hospital
        return HttpResponse('Gender:' + x + '<br>' +'Last_name:' + y + '<br>' + 'Email_id:' + z + '<br>' + 'Qualification:'+ l +'<br>'+'Locality:'+ k +'<br>'+ 'Hospital:' + o + '<br>'+'<input type="button" value="Accept">' + '<input type="button" value="Reject">')
    else:
        data = Rmplist.objects.all()

        return render(request, 'myapp/rmplist.html', {'data':data})



def home(request):
    return render(request, 'myapp/home.html')
def payment(request):
    return render(request, 'myapp/payment.html')
def appointment(request):
    return render(request, 'myapp/appointment.html')
def feedback(request):
    return render(request, 'myapp/feedback.html')


class PostListView(ListView):
    model = Post
    template_name = 'myapp/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5


class UserPostListView(ListView):
    model = Post
    template_name = 'myapp/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
