
from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import home, contact_page, login_page, register_page, about, contact, how_we_work
from carts.views import cart_home
from django.conf.urls import url
from django.conf import settings
from django.contrib import admin
from django.conf.urls import url, include
from .views import home_page, login_page, register_page,log_out
from django.contrib.auth import views as auth_views
from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('logout/', log_out, name='logout'),
    path('contact_page/', contact_page , name='contact_page'),
    path('contact/', contact , name='contact'),
    path('about/', about , name='about'),
    path('how_we_work/', how_we_work , name='how_we_work'),

    url(r'^doctor/', include(("doctor_home.url","doctor"), namespace= 'doctor')),
    #(r'^$',home_page , name='home_page'),
    url(r'^login/$', login_page, name='login' ),
    url(r'^register/$', register_page, name='register' ),
    url(r'^password/change/$',
        auth_views.PasswordChangeView.as_view(),
        name='password_change'),
    url(r'^password/change/done/$',
        auth_views.PasswordChangeDoneView.as_view(),
        name='password_change_done'),
    url(r'^password/reset/$',
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

    path('search/', include('search.urls')),
    path('cart/', cart_home, name='cart_home'),
    url(r'^chat/', include('chat.url')),

    path('profile/',include('doctor_profile.urls')),
    path('prescription/',include('prescription.urls')),
    path('work_history/',include('work_history.urls')),
    path('rmp/',include('rmp.urls')),

    path('admin/', admin.site.urls),
    path('admin1/', user_views.register, name='register'),
    path('admin1/profile/', user_views.profile, name='profile'),
    path('admin1/login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('admin1/logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'),
         name='logout'),
    path('admin1/password_reset/',
         auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'),
         name='password_reset'),
    path('admin1/password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
         name='password_reset_done'),
    path('admin1/password_reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('admin1/password_reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
         name='password_reset_complete'),
    path('doctor/', include('doctor_profile.urls')),
    path('', include('myapp.urls'), name='myapp'),
    path('rmp/', include('rmp.urls')),
]

if settings.DEBUG:

    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
