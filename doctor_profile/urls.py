from django.conf.urls import url
from django.urls import path
from . import views
app_name='doctor_profile'
urlpatterns=[
    path('',views.index,name='index'),
    path('make_profile/',views.make_profile,name='make_profile'),
    path('modify_profile/',views.modify_profile,name='modify_profile'),
    path('show_profile/',views.Show_Profile,name='show_profile'),
    path('date_add/',views.DateCreate.as_view(),name='Date_Create'),
    #url(r'^(?P<pk>[0-9]+)/$',views.DetailView.as_view(),name='date_detail'),
    path('date_create/',views.date_create,name='date_create'),
    url(r'^(?P<pk>[0-9]+)/slot/$', views.create_slot, name='create_slot'),

    #path('make_profile/',views.make_profie,name='make_profie'),
    #path('add_profile/',views.add_profile,name='add_profile'),
    #path('make_profile1/',views.ProfileCreate.as_view(),name='make_profile1'),
    #path('show_profile/<str:doctor_id>',views.Show_Profile,name='show_profile'),
    #path('modify_profile/'views.Modify_Profile_Databse,name='modify_profile'),
    ]
