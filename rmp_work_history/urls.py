from django.conf.urls import url
from django.urls import path
from . import views


app_name='rmp_work_history'

urlpatterns=[
path('upcoming/',views.index, name='rmp_work_history'),
path('history',views.history, name='rmp_history'),

 ]
