from django.conf.urls import url
from django.urls import path
from . import views

appname='disease'
urlpatterns = [
    # url(r'^(?P<string>[\w\-]+)/$',views.home,name='home'),
    path('',views.disease,name='data'),
]
