from django.conf.urls import url
from django.urls import path
from . import views
from rmp.views import user_register, new_user_reg
from django.contrib.auth import views as auth_views
from users import views as user_views

app_name='rmp'

urlpatterns=[
    path('make_rmp_profile/',views.make_profile,name='make_rmp_profile'),
    path('modify_rmp_profile/',views.modify_profile,name='modify_rmp_profile'),
    path('show_rmp_profile/',views.Show_Profile,name='show_rmp_profile'),
    path('login/',views.login_page,name='login_rmp_profile'),
   # path('register/',views.register_page,name='make_rmp_profile'),
   url(r'^rmp/register/$',views.user_register , name='user_register' ),
   url(r'^rmp/new_user_reg/$',views.new_user_reg , name='new_user_reg' ),
   url(r'^password/change/$',
        auth_views.PasswordChangeView.as_view(),
        name='password_change'),
    url(r'^password/change/done/$',
        auth_views.PasswordChangeDoneView.as_view(),
        name='password_change_done'),
    url(r'^login/password/reset/$',
        auth_views.PasswordResetView.as_view(),
        name='password_reset'),
    url(r'^password/reset/done/$',
        auth_views.PasswordResetDoneView.as_view(),
        name='password_reset_done'),
    url(r'^password/reset/\
        (?P<uidb64>[0-9A-Za-z_\-]+)/\
        (?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.PasswordResetConfirmView.as_view(),
        name='password_reset_confirm'),
    url(r'^password/reset/complete/$',
        auth_views.PasswordResetCompleteView.as_view(),
        name='password_reset_complete'),

    ]
