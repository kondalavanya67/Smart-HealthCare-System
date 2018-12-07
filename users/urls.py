from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    #path('admin1/', views.register, name='register_admin'),
    path('admin1/profile/', views.profile1, name='profile_admin'),
    path('admin1/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login_admin'),
    path('admin1/logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'),
         name='logout_admin'),
    path('admin1/password_reset/',
          auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'),
          name='admin1_password_reset'),
     path('admin1/password_reset/done/',
          auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
          name='admin1_password_reset_done'),
     path('admin1/password_reset-confirm/<uidb64>/<token>/',
          auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
          name='admin1_password_reset_confirm'),
     path('admin1/password_reset-complete/',
          auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
          name='admin1_password_reset_complete'),
]

if settings.DEBUG:

    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)