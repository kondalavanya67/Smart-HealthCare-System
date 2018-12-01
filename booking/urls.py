from django.urls import path
from booking import views

app_name='booking'
urlpatterns = [
    path('search/',views.doctor_list, name="doctor_list"),
    path('search/<pk>/',views.doctor_detail, name='doctor_detail'),
    path('enter_paitent_details/<pk>/',views.enter_paitent_details, name='enter_paitent_details'),
    path('view_paitent_details/<pk>/',views.view_paitent_details, name='view_paitent_details'),
    # path('make_slot/<pk>',views.make_slot,name='make_slot'),
    # path('booking_confirmation/<pk>/', views.booking_confirmation, name='booking_confirmation')
    path('booking_confirmation/<pk>/', views.AppointmentDetialsCreate.as_view(), name='booking_confirmation'),\
    path('ajax/load-slots/', views.load_time, name='ajax_load_slots'),


]
