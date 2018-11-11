from django.conf.urls import url
from django.urls import path
from . import views
app_name='doctor_profile'
urlpatterns=[
    path('',views.index,name='index'),
    path('make_profile/',views.make_profile,name='make_profile'),
    path('modify_profile/<str:doctor_id>',views.modify_profile,name='modify_profile'),
    path('show_profile/<str:doctor_id>',views.Show_Profile,name='show_profile'),
    #path('make_profile/',views.make_profie,name='make_profie'),
    #path('add_profile/',views.add_profile,name='add_profile'),
    #path('make_profile1/',views.ProfileCreate.as_view(),name='make_profile1'),
    #path('show_profile/<str:doctor_id>',views.Show_Profile,name='show_profile'),
    #path('modify_profile/'views.Modify_Profile_Databse,name='modify_profile'),
    ]
