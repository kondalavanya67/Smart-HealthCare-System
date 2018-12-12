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

# #myapp
    def test_detail_url_14(self):
        path1=reverse('myapp:adminpage')
        assert resolve(path1).view_name == 'myapp:adminpage'
    def test_detail_url_15(self):
        path1=reverse('myapp:myapp-index')
        assert resolve(path1).view_name == 'myapp:myapp-index'
    def test_detail_url_16(self):
        path1=reverse('myapp:myapp-rmpdetails')
        assert resolve(path1).view_name == 'myapp:myapp-rmpdetails'
    def test_detail_url_17(self):
        path1=reverse('myapp:myapp-fullrmplist',kwargs={'pk':1})
        assert resolve(path1).view_name == 'myapp:myapp-fullrmplist'
    def test_detail_url_18(self):
        path1=reverse('myapp:myapp-rmpdetail')
        assert resolve(path1).view_name == 'myapp:myapp-rmpdetail'
    def test_detail_url_19(self):
        path1=reverse('myapp:myapp-patientdetail',kwargs={'pk':1})
        assert resolve(path1).view_name == 'myapp:myapp-patientdetail'
    def test_detail_url_20(self):
        path1=reverse('myapp:rmp_upcoming_appointments',kwargs={'pk':1})
        assert resolve(path1).view_name == 'myapp:rmp_upcoming_appointments'
    def test_detail_url_21(self):
        path1=reverse('myapp:rmp_attended_appointments',kwargs={'pk':1})
        assert resolve(path1).view_name == 'myapp:rmp_attended_appointments'
    def test_detail_url_22(self):
        path1=reverse('myapp:myapp-payment')
        assert resolve(path1).view_name == 'myapp:myapp-payment'
    def test_detail_url_23(self):
        path1=reverse('myapp:doctor_verification_required')
        assert resolve(path1).view_name == 'myapp:doctor_verification_required'
    def test_detail_url_24(self):
        path1=reverse('myapp:myapp-appointment')
        assert resolve(path1).view_name == 'myapp:myapp-appointment'
    def test_detail_url_25(self):
        path1=reverse('myapp:myapp-feedback')
        assert resolve(path1).view_name == 'myapp:myapp-feedback'
    def test_detail_url_26(self):
        path1=reverse('myapp:doctor_detail',kwargs={'pk':1})
        assert resolve(path1).view_name == 'myapp:doctor_detail'
    def test_detail_url_27(self):
        path1=reverse('myapp:doctor_upcoming_appointments',kwargs={'pk':1})
        assert resolve(path1).view_name == 'myapp:doctor_upcoming_appointments'
    def test_detail_url_28(self):
        path1=reverse('myapp:doctor_attended_appointments',kwargs={'pk':1})
        assert resolve(path1).view_name == 'myapp:doctor_attended_appointments'
    def test_detail_url_29(self):
        path1=reverse('myapp:doctor_slot',kwargs={'pk':1})
        assert resolve(path1).view_name == 'myapp:doctor_slot'
    def test_detail_url_31(self):
        path1=reverse('myapp:verify',kwargs={'pk':1})
        assert resolve(path1).view_name == 'myapp:verify'
    def test_detail_url_32(self):
        path1=reverse('myapp:rmp_appointments_past',kwargs={'pk':1})
        assert resolve(path1).view_name == 'myapp:rmp_appointments_past'

##rmp_work_history

    def test_detail_url_33(self):
        path1=reverse('rmp_work_history:rmp_work_history')
        assert resolve(path1).view_name == 'rmp_work_history:rmp_work_history'
    def test_detail_url_34(self):
        path1=reverse('rmp_work_history:rmp_history')
        assert resolve(path1).view_name == 'rmp_work_history:rmp_history'

##shopping_cart

    def test_detail_url_35(self):
        path1=reverse('shopping_cart:add_to_cart',kwargs={'item_id':1})
        assert resolve(path1).view_name == 'shopping_cart:add_to_cart'
    def test_detail_url_36(self):
        path1=reverse('shopping_cart:order_summary')
        assert resolve(path1).view_name == 'shopping_cart:order_summary'
    def test_detail_url_37(self):
        path1=reverse('shopping_cart:enter_address')
        assert resolve(path1).view_name == 'shopping_cart:enter_address'
    def test_detail_url_38(self):
        path1=reverse('shopping_cart:delete_from_cart',kwargs={'item_id':1})
        assert resolve(path1).view_name == 'shopping_cart:delete_from_cart'
    def test_detail_url_39(self):
        path1=reverse('shopping_cart:delete_from_cart2',kwargs={'item_id':1})
        assert resolve(path1).view_name == 'shopping_cart:delete_from_cart2'
    def test_detail_url_40(self):
        path1=reverse('shopping_cart:purchase_success')
        assert resolve(path1).view_name == 'shopping_cart:purchase_success'
    def test_detail_url_41(self):
        path1=reverse('shopping_cart:purchase_success_cod')
        assert resolve(path1).view_name == 'shopping_cart:purchase_success_cod'
    def test_detail_url_42(self):
        path1=reverse('shopping_cart:order')
        assert resolve(path1).view_name == 'shopping_cart:order'
    def test_detail_url_43(self):
        path1=reverse('shopping_cart:order_summary_ajax')
        assert resolve(path1).view_name == 'shopping_cart:order_summary_ajax'
    
##shoppingPortalApp   
    def test_detail_url_44(self):
        path1=reverse('shoppingPortalApp:main')
        assert resolve(path1).view_name == 'shoppingPortalApp:main'
    def test_detail_url_45(self):
        path1=reverse('shoppingPortalApp:add_medicine')
        assert resolve(path1).view_name == 'shoppingPortalApp:add_medicine'
    def test_detail_url_46(self):
        path1=reverse('shoppingPortalApp:successful_add')
        assert resolve(path1).view_name == 'shoppingPortalApp:successful_add'
    def test_detail_url_47(self):
        path1=reverse('shoppingPortalApp:result')
        assert resolve(path1).view_name == 'shoppingPortalApp:result'
    def test_detail_url_48(self):
        path1=reverse('shoppingPortalApp:medicine',kwargs={'name':1})
        assert resolve(path1).view_name == 'shoppingPortalApp:medicine'
    def test_detail_url_49(self):
        path1=reverse('shoppingPortalApp:del_edit_medicine')
        assert resolve(path1).view_name == 'shoppingPortalApp:del_edit_medicine'
    def test_detail_url_50(self):
        path1=reverse('shoppingPortalApp:delete',kwargs={'med_id':1})
        assert resolve(path1).view_name == 'shoppingPortalApp:delete'
    def test_detail_url_51(self):
        path1=reverse('shoppingPortalApp:update_medicine',kwargs={'med_id':1})
        assert resolve(path1).view_name == 'shoppingPortalApp:update_medicine'

##show_appointments
    def test_detail_url_52(self):
        path1=reverse('show_appointments:index')
        assert resolve(path1).view_name == 'show_appointments:index'
    def test_detail_url_53(self):
        path1=reverse('show_appointments:show_slots')
        assert resolve(path1).view_name == 'show_appointments:show_slots'

##website
    def test_detail_url_54(self):
        path1=reverse('home')
        assert resolve(path1).view_name == 'home'
    def test_detail_url_55(self):
        path1=reverse('logout')
        assert resolve(path1).view_name == 'logout'
    def test_detail_url_56(self):
        path1=reverse('contact_page')
        assert resolve(path1).view_name == 'contact_page'
    def test_detail_url_57(self):
        path1=reverse('contact')
        assert resolve(path1).view_name == 'contact'
    def test_detail_url_58(self):
        path1=reverse('contact_doctor')
        assert resolve(path1).view_name == 'contact_doctor'
    def test_detail_url_59(self):
        path1=reverse('about')
        assert resolve(path1).view_name == 'about'
    def test_detail_url_60(self):
        path1=reverse('how_we_work')
        assert resolve(path1).view_name == 'how_we_work'
    def test_detail_url_61(self):
        path1=reverse('doctor_home')
        assert resolve(path1).view_name == 'doctor_home'
    def test_detail_url_63(self):
        path1=reverse('login')
        assert resolve(path1).view_name == 'login'
    def test_detail_url_64(self):
        path1=reverse('user_register')
        assert resolve(path1).view_name == 'user_register'
    def test_detail_url_65(self):
        path1=reverse('new_user_reg')
        assert resolve(path1).view_name == 'new_user_reg'
    def test_detail_url_66(self):
        path1=reverse('password_change')
        assert resolve(path1).view_name == 'password_change'
    def test_detail_url_67(self):
        path1=reverse('password_change_done')
        assert resolve(path1).view_name == 'password_change_done'
    def test_detail_url_68(self):
        path1=reverse('password_reset')
        assert resolve(path1).view_name == 'password_reset'
    def test_detail_url_69(self):
        path1=reverse('password_reset_done')
        assert resolve(path1).view_name == 'password_reset_done'
    def test_detail_url_70(self):
        path1=reverse('password_reset_complete')
        assert resolve(path1).view_name == 'password_reset_complete'
    
    

