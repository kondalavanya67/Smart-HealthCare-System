from django.test import RequestFactory
from django.urls import reverse
from django.contrib.auth.models import User, AnonymousUser
from disease.views import disease
from mixer.backend.django import mixer
import pytest

@pytest.mark.django_db
class TestViews:
    def test_disease_authenticated(self):
        path=reverse('data')
        request=RequestFactory().get(path)
        request.user=mixer.blend(User)
        response=disease(request)
        assert response.status_code == 200

    # def test_disease_unauthenticated(self):
    #     path=reverse('data')
    #     request=RequestFactory().get(path)
    #     request.user=mixer.blend(AnonymousUser)
    #     response=AnonymousUser()
    #     assert response.status_code == 200
