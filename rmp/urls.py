from django.conf.urls import url
from django.urls import path
from . import views
app_name='rmp'

urlpatterns=[
    path('make_rmp_profile/',views.make_profile,name='make_rmp_profile'),
    path('modify_rmp_profile/',views.modify_profile,name='modify_rmp_profile'),
    path('show_rmp_profile/',views.Show_Profile,name='show_rmp_profile'),
    path('login/',views.login_page,name='make_rmp_profile'),
    path('register/',views.register_page,name='make_rmp_profile'),
    ]
