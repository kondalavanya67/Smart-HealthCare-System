from django.conf.urls import url
from django.urls import path
from . import views
from rest_framework import routers
from .views import DoctorProfileViewSet,RmpProfileViewSet,PaitentDetailsViewSet,AppointmentDetialsViewSet,SlotViewSet

app_name='restframework'



router = routers.DefaultRouter()
router.register(r'doctor', DoctorProfileViewSet)
router.register(r'rmp', RmpProfileViewSet)
router.register(r'appointments', AppointmentDetialsViewSet)
router.register(r'paitent_details', PaitentDetailsViewSet)
router.register(r'slot', SlotViewSet)



urlpatterns = router.urls