from django.urls import path
from shoppingPortalApp import views


urlpatterns = [
    path('ShopOnline/main/',views.index),
    path('ShopOnline/add/',views.index_add),
    path('ShopOnline/main/search/',views.result, name='result'),
    path('ShopOnline/main/<name>/',views.showMedicine_name, name='medicine'),
    path('ShopOnline/delete/<id>/',views.index_delete),
]