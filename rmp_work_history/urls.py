from django.conf.urls import url
from django.urls import path
from . import views


app_name='rmp_work_history'

urlpatterns=[
path('',views.index, name='rmp_work_history'),
 ];
