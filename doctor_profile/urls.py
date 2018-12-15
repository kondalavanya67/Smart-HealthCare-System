from django.conf.urls import url
from django.urls import path
from . import views
from rest_framework import routers
from .views import ProfileViewSet

app_name='doctor_profile'
urlpatterns=[
    path('',views.index,name='index'),
    path('make_profile/',views.make_profile,name='make_profile'),
    path('modify_profile/',views.modify_profile,name='modify_profile'),
    path('show_profile/',views.Show_Profile,name='show_profile'),
    path('date_add/',views.DateCreate.as_view(),name='Date_Create'),
    path('date_create/',views.date_create,name='date_create'),
    url(r'^date_add/(?P<pk>[0-9]+)/slot/$', views.create_slot, name='create_slot'),
    path('verification_required/',views.verification,name='verification')

    ]
