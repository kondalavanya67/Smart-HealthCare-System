from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from . models import Post
from django.contrib.auth.models import User
from django.views.generic import ListView,DetailView, CreateView, UpdateView,DeleteView

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'myapp/home.html',context)


class PostListView(ListView):
    model = Post
    template_name = 'myapp/home.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

class UserPostListView(ListView):
    model = Post
    template_name = 'myapp/user_posts.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(doctor_name=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['doctor_id','doctor_name','speciality']

    def form_valid(self, form):
        form.instance.doctor_name = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['doctor_id','doctor_name','speciality']

    def form_valid(self, form):
        form.instance.doctor_name = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.doctor_name:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = "/"

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.doctor_name:
            return True
        return False