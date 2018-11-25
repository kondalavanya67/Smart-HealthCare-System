from django.conf.urls import url
from django.urls import path
from . import views
app_name='prescription'
urlpatterns=[
    path('',views.index,name='index'),
    path('make_prescription/',views.make_prescription,name='make_prescription'),
    #path('<int:prescription_id>/',views.detail,name='detail'),
    url(r'^prescription_add/(?P<appointment_id>[0-9]+)$',views.PrescriptionCreate.as_view(),name='Prescription_Add1'),
    path('prescription_add/',views.make_prescription,name='Prescription_Add'),
    url(r'^(?P<pk>[0-9]+)/$',views.DetailView.as_view(),name='detail'),
    url(r'^(?P<prescription_id>[0-9]+)/create_item/$', views.create_item, name='create_item'),
    #url(r'^name-autocomplete/$',views.MedicineAutocomplete.as_view(),name='name-autocomplete'),
    path('name-autocomplete/',views.MedicineAutocomplete.as_view(),name='name-autocomplete'),
    url(r'^(?P<prescription_id>[0-9]+)/print/$', views.print, name='print'),


    #path('prescription_add1/',views.dummy,name='Prescription_Add1'),
]
