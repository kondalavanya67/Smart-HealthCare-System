from django.urls import path
from payment import views

app_name = 'payment'

urlpatterns = [
	path('online-payment/',views.payment_online_cod,name='payment_online_cod'),
]