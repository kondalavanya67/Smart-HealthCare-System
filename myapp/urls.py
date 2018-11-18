from .views import PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView,UserPostListView
from django.conf.urls import url
from . import views

urlpatterns = [

    url('^admin1/doctorlist/$', views.index, name='myapp-index'),
    url('^admin1/rmplist/$', views.rmpdetails, name='myapp-rmpdetails'),
    url('^admin1/home/$', PostListView.as_view(), name='myapp-home'),
    url('^admin1/payment/',views.payment,name='myapp-payment'),
    url('^admin1/appointment/',views.appointment,name='myapp-appointment'),
    url('^admin1/feedback/',views.feedback,name='myapp-feedback'),
    url('^admin1/user/<str:username>$', UserPostListView.as_view(), name='user-posts'),
    url('^admin1/post/<int:pk>/$', PostDetailView.as_view(), name='post-detail'),
    url('^admin1/post/new/$', PostCreateView.as_view(), name='post-create'),
    url('^admin1/post/<int:pk>/update/$', PostUpdateView.as_view(), name='post-update'),
    url('^admin1/post/<int:pk>/delete/$', PostDeleteView.as_view(), name='post-delete'),
]
