from django.urls import path
from shoppingPortalApp import views

app_name = 'shoppingPortalApp'

urlpatterns = [
    path('',views.index,name='main'),
    path('add/',views.index_add,name='add_medicine'),
    path('added/',views.added,name='successful_add'),
    path('main/search/',views.result, name='result'),
    path('main/<name>/',views.showMedicine_name, name='medicine'),
    path('delete/',views.index_delete,name='del_medicine'),
]