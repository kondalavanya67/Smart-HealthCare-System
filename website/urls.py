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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('contact_page/', contact_page , name='contact_page'),
    path('contact/', contact , name='contact'),
    path('about/', about , name='about'),
    path('how_we_work/', how_we_work , name='how_we_work'),
    path('login/', login_page , name='login'),
    path('register/', register_page , name='register'),
    path('doctor/', include('doctor.urls')),
    path('search/', include('search.urls')),
    path('cart/', cart_home, name='cart_home'),
    url(r'^chat/', include('chat.url')),
    path('ShopOnline/', include('shoppingPortalApp.urls')),
]

if settings.DEBUG:

    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

