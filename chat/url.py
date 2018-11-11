
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^(?P<room_id>[^/]+)', views.home),
    url(r'^rooms/(?P<room_id>[^/]+)/messages/', views.messages),
]