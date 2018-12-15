from mixer.backend.django import mixer
from django.test import TestCase
import pytest

@pytest.mark.django_db
class TestModels(TestCase):

    def test_self_ini_profile(self):
        profile=mixer.blend('doctor_profile.Profile',pk=100)
        self.assertEqual(str(profile), str(100))
