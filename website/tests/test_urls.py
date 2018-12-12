from django.urls import reverse,resolve
from disease import urls
from doctor_profile import urls

class TestUrls:
# Disease APP
    def test_detail_url(self):
        path1=reverse('data')
        assert resolve(path1).view_name == 'data'

# Doctor Profile App
    def test_detail_url_1(self):
        path1=reverse('doctor_profile:make_profile')
        assert resolve(path1).view_name == 'doctor_profile:make_profile'

    def test_detail_url_2(self):
        path1=reverse('doctor_profile:modify_profile')
        assert resolve(path1).view_name == 'doctor_profile:modify_profile'
    def test_detail_url_3(self):
        path1=reverse('doctor_profile:show_profile')
        assert resolve(path1).view_name == 'doctor_profile:show_profile'
    def test_detail_url_4(self):
        path1=reverse('doctor_profile:Date_Create')
        assert resolve(path1).view_name == 'doctor_profile:Date_Create'
    def test_detail_url_5(self):
        path1=reverse('doctor_profile:date_create')
        assert resolve(path1).view_name == 'doctor_profile:date_create'
    def test_detail_url_6(self):
        path1=reverse('doctor_profile:create_slot',kwargs={'pk':1})
        assert resolve(path1).view_name == 'doctor_profile:create_slot'
    def test_detail_url_7(self):
        path1=reverse('doctor_profile:verification')
        assert resolve(path1).view_name == 'doctor_profile:verification'

# #Prescription
    def test_detail_url_8(self):
        path1=reverse('prescription:index')
        assert resolve(path1).view_name == 'prescription:index'
    def test_detail_url_9(self):
        path1=reverse('prescription:Prescription_Add1',kwargs={'appointment_id':1})
        assert resolve(path1).view_name == 'prescription:Prescription_Add1'
    def test_detail_url_10(self):
        path1=reverse('prescription:detail',kwargs={'pk':1})
        assert resolve(path1).view_name == 'prescription:detail'
    def test_detail_url_11(self):
        path1=reverse('prescription:create_item',kwargs={'prescription_id':1})
        assert resolve(path1).view_name == 'prescription:create_item'
    def test_detail_url_12(self):
        path1=reverse('prescription:name-autocomplete')
        assert resolve(path1).view_name == 'prescription:name-autocomplete'
    def test_detail_url_13(self):
        path1=reverse('prescription:print',kwargs={'prescription_id':1})
        assert resolve(path1).view_name == 'prescription:print'
