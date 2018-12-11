from django.urls import path
from shoppingPortalApp import views

app_name = 'shoppingPortalApp'

urlpatterns = [
    path('',views.index,name='main'),
    path('add/',views.index_add,name='add_medicine'),
    path('action/<name>/',views.added,name='successful_add'),
    path('search/',views.result, name='result'),
    path('main/<name>/',views.showMedicine_name, name='medicine'),
    path('delete-edit/',views.index_delete_edit,name='del_edit_medicine'),
    path('delete/<med_id>',views.delete,name='delete'),
    path('edit/<med_id>',views.update_medicine,name='update_medicine'),
]