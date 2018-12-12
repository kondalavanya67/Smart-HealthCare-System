from mixer.backend.django import mixer
from django.test import TestCase
import pytest
from django.contrib.auth.models import User
from django.utils import timezone
import datetime
from doctor_profile.models import Profile, BookingDate, Slot
from prescription.models import Prescription, Item

@pytest.mark.django_db
class TestModels(TestCase):
    def setUp(self):
        user1 = User.objects.create(username='testuser1', password='HelloWorld@123', email='testuser1@gmail.com')
        # User.objects.create(username='testuser2', password='helloworld@123', email='testuser2@gmail.com')
        Profile.objects.create(
        	user=user1,
        	verified=True,
            profile_photo='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSGTVf63Vm3XgOncMVSOy0-jSxdMT8KVJIc8WiWaevuWiPGe0Pm',
        	first_name="ShivamG",
        	last_name="Gupta",
            dob=datetime.datetime.now(),
            gender='Male',
            email_id=user1.email,
            mobile_no='9411329082',
            speciality='ORTHOPAEDIC',
            qualification='MBSS',
            locality='Chennai',
            hospital='SIMS',)
        profile1= Profile.objects.get(first_name="ShivamG")
        BookingDate.objects.create(
            doctor=profile1,
            date=datetime.datetime.now(),
        )

        Prescription.objects.create(
            doctor=profile1,
            prescription_id=1,
            prescription_date=datetime.datetime.now(),
            pdf='https://pdfs.semanticscholar.org/22b9/ed9f743cad723b6a08f51d76b66d947997e0.pdf'
        )
        prescription1=Prescription.objects.get(prescription_id=1)
        Item.objects.create(
            prescription=prescription1,
            medicine_name='Rustox',
            days=1,
            morning='True',
            afternoon='True',
            night='True',


        )
###################DOCTOR PROFILE #########################
    def test_self_ini_profile(self):
        profile= Profile.objects.get(first_name="ShivamG")
        self.assertEqual(str(profile), str(1))

    def test_get_absolute_url(self):
        profile= Profile.objects.get(first_name="ShivamG")
        self.assertEqual(profile.get_absolute_url(), '/rmp/booking/search/1/')

    def test_get_absolute_url_show(self):
        profile= Profile.objects.get(first_name="ShivamG")
        self.assertEqual(profile.get_absolute_url_show(), '/admin1/doctorlist/search/1/')
    def test_get_absolute_url_upcoming_appointments(self):
        profile= Profile.objects.get(first_name="ShivamG")
        self.assertEqual(profile.get_absolute_url_upcoming_appointments(), '/admin1/doctorlist/search/doctor_upcoming_appointments/1/')
    def test_absolute_url_attended_appointments(self):
        profile= Profile.objects.get(first_name="ShivamG")
        self.assertEqual(profile.get_absolute_url_attended_appointments(), '/admin1/doctorlist/search/doctor_attended_appointments/1/')
    def test_absolute_url_booking(self):
        profile= Profile.objects.get(first_name="ShivamG")
        self.assertEqual(profile.get_absolute_url_booking(), '/rmp/booking/enter_paitent_details/1/')
#########################BOOKING DATE ########################
    def test_bookingdate_self_function(self):
        profile1= Profile.objects.get(first_name="ShivamG")
        date1=BookingDate.objects.get(doctor=profile1)
        self.assertEqual(str(date1), str(datetime.datetime.now().date()))

    def test_bookingdate_get_absolute_url(self):
        profile1= Profile.objects.get(first_name="ShivamG")
        date1=BookingDate.objects.get(doctor=profile1)
        self.assertEqual(date1.get_absolute_url(), "/profile/date_add/1/slot/")

######################## PRESCRIPTION #########################
    def test_prescription_self_function(self):
        prescription= Prescription.objects.get(prescription_id=1)
        self.assertEqual(str(prescription), str(1))

    def test_prescription_get_absolute_url(self):
        prescription= Prescription.objects.get(prescription_id=1)
        self.assertEqual(prescription.get_absolute_url(), '/prescription/1/')
######################## ITEMS ##################################
    def test_item_self_function(self):
        prescription= Prescription.objects.get(prescription_id=1)
        item=Item.objects.get(prescription=prescription)
        self.assertEqual(str(item),'Rustox')
