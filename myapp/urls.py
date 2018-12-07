from django.conf.urls import url
from django.urls import include
from . import views

urlpatterns = [
    url('^admin1/adminpage/$',views.adminpage,name='adminpage'),
    url('^admin1/doctorlist/$', views.index, name='myapp-index'),
    url('^admin1/doctorlist/fullview' ,views.fullviewdoc,name='myapp-fullindex'),
    url('^admin1/rmplist/$', views.rmpdetails, name='myapp-rmpdetails'),
    url('^admin1/rmplist/fullview',views.fullviewrmp, name='myapp-fullrmplist'),
    url('^admin1/payment/',views.payment,name='myapp-payment'),
    url('^admin1/appointment/',views.appointment,name='myapp-appointment'),
    url('^admin1/feedback/',views.feedback,name='myapp-feedback'),
    url('',include('users.urls')),
]
