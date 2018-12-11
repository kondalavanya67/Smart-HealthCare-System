
from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import home, contact_page, login_page, about, contact, how_we_work,doctor_home,doctor_contact
from django.conf.urls import url
from django.conf import settings
from django.contrib import admin
from django.conf.urls import url, include


from .views import home_page, login_page,log_out,user_register, new_user_reg

from django.contrib.auth import views as auth_views
from users import views as user_views

# app_name='website'
urlpatterns = [

    path('', home, name='home'),
    path('admin/',admin.site.urls),
    path('logout/', log_out, name='logout'),
    path('contact_page/', contact_page , name='contact_page'),
    path('contact/', contact , name='contact'),
    path('doctor_contact/', doctor_contact , name='contact_doctor'),
    path('about/', about , name='about'),
    path('how_we_work/', how_we_work , name='how_we_work'),
    url(r'^doctor_home/$',doctor_home, name='doctor_home'),
    # url(r'^doctor_home/$',doctor_verification_required, name='doctor_verification_required'),
    url(r'^doctor/', include(("doctor_home.url","doctor"), namespace= 'doctor')),
    #(r'^$',home_page , name='home_page'),
    url(r'^login/$', login_page, name='login' ),
    url(r'^doctor/register/$',user_register , name='user_register' ),
    url(r'^doctor/new_user_reg/$',new_user_reg , name='new_user_reg' ),
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

<<<<<<< HEAD
    path('search/', include('search.urls')),
    path('restframework/', include('restframework.urls')),
=======
   
>>>>>>> 4bfaaa03ba4c18689d6a17676e9e405ea7c5a376



    path('shoponline/', include('shoppingPortalApp.urls')),
    path('shoponline/', include('shopping_cart.urls')),
    path('profile/',include('doctor_profile.urls')),
    path('disease/',include('disease.urls')),
    path('prescription/',include('prescription.urls')),
    path('rmp/booking/',include('booking.urls')),
    path('appointments/',include('show_appointments.urls'),name='show_appointments'),
    path('work_history/',include('work_history.urls')),
    path('rmp_work_history/',include('rmp_work_history.urls')),
    #url(r'^activate/$', activate, name='activate'),

    #path('account-activation-email-sent', account_activation_email_sent, name='account_activation_email_sent'),
   # path('activate/<uidb64>/<token>', activate_account, name='activate'),
  #  path('resend-activation-link', generate_new_activation_link, name='resend_activation_link'),
<<<<<<< HEAD
    path('admin/', admin.site.urls),
=======
>>>>>>> 4bfaaa03ba4c18689d6a17676e9e405ea7c5a376
    path('', include('myapp.urls'), name='myapp'),
    path('users/',include('users.urls'), name='users'),
    path('rmp/', include('rmp.urls')),
]

if settings.DEBUG:

    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
