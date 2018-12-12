from django.conf.urls import url
from django.urls import path
from . import views
from rest_framework import routers
from .views import DoctorProfileViewSet,RmpProfileViewSet,PaitentDetailsViewSet,AppointmentDetialsViewSet,SlotViewSet
from doctor_profile.models import Profile,Slot
from rmp.models import rmpContact
from booking.models import AppointmentDetials,PaitentDetails
app_name='restframework'



router = routers.DefaultRouter()
router.register(r'doctor', DoctorProfileViewSet, base_name='Profile')
router.register(r'rmp', RmpProfileViewSet, base_name='rmpContact')
router.register(r'appointments', AppointmentDetialsViewSet, base_name='AppointmentDetials')
router.register(r'paitent_details', PaitentDetailsViewSet, base_name='PaitentDetails')
router.register(r'slot', SlotViewSet)



urlpatterns = router.urls
