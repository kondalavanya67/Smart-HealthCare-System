"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
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
from .views import home_page, login_page, register_page
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
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
    url(r'^chat/', include('chat.url'))



]

if settings.DEBUG:

    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

