from django.conf.urls import url,include
from .views import doctor_home_page

urlpatterns=[
url(r'^$', doctor_home_page, name="doctor_home_page"),

]