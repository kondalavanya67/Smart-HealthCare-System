from django.conf.urls import url
from django.urls import include
from django.urls import path
from . import views
from django.urls import path
app_name="myapp"
urlpatterns = [
    url('^admin1/adminpage/$',views.adminpage,name='adminpage'),
    url('^admin1/doctorlist/$', views.index, name='myapp-index'),
    url('^admin1/rmplist/$', views.rmpdetails, name='myapp-rmpdetails'),
    path('admin1/rmplist/search/<pk>/',views.fullviewrmp, name='myapp-fullrmplist'),
    path('admin1/rmplist/fullview/rmpdetail/',views.rmpdetail,name='myapp-rmpdetail'),
    path('admin1/rmplist/fullview/patientdetails/<pk>/',views.patientdetails,name='myapp-patientdetail'),
    path('admin1/rmplist/search/rmp_upcoming_appointments/<pk>/', views.rmp_upcoming_appointments,name='rmp_upcoming_appointments'),
    path('admin1/rmplist/search/rmp_attended_appointments/<pk>/', views.rmp_attended_appointments,name='rmp_attended_appointments'),
    url('^admin1/payment/',views.payment,name='myapp-payment'),
    url('^admin1/doctor_verification/',views.doctor_verify,name='doctor_verification_required'),
    url('^admin1/rmp_verification/',views.rmp_verify,name='rmp_verification_required'),

    url('^admin1/appointment/',views.appointment,name='myapp-appointment'),
    url('^admin1/feedback/',views.feedback,name='myapp-feedback'),
    path('admin1/doctorlist/search/<pk>/',views.doctor_detail, name='doctor_detail'),
    path('admin1/doctorlist/search/doctor_upcoming_appointments/<pk>/',views.doctor_upcoming_appointments, name='doctor_upcoming_appointments'),
    path('admin1/doctorlist/search/doctor_attended_appointments/<pk>/',views.doctor_attended_appointments, name='doctor_attended_appointments'),
    path('admin1/doctorlist/search/slot/<pk>/',views.show_slots, name='doctor_slot'),
    path('admin1/doctor_verification/verify', views.doctor_verify_confirmation, name='doctor_verify'),
    # path('admin1/doctor_verification/verify/<pk>/',views.a, name='doctor_verify'),
    path('admin1/s/<pk>/',views.doctor_verify_confirmation,name='verify'),
    path('admin1/r/<pk>/',views.rmp_verify_confirmation,name='verify-rmp'),

    path('admin1/rmp_appointments_past/<pk>/',views.rmp_appointments_past, name='rmp_appointments_past'),

    url('',include('users.urls')),
]
