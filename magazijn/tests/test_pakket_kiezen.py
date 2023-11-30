from django.test import TestCase, RequestFactory
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta

from magazijn.models import Pakket, Klant
from magazijn.views import ChoicePackage


class ChoicePackageTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.url = reverse('choice-package')

    def test_get(self):
        # Create test data
        seven_days_ago = timezone.now() - timedelta(days=7)
        pakket = Pakket.objects.create(gezinsnaam='Test Gezinsnaam', aangemaakt_op=seven_days_ago)
        klant = Klant.objects.create(name='Test Klant')

        request = self.factory.get(self.url)
        request.user = self.user

        response = ChoicePackage.as_view()(request)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'magazijn/pakket_kiezen.html')
        self.assertEqual(len(response.context_data['klanten_page']), 1)
        self.assertEqual(response.context_data['klanten_page'][0], klant)

    def test_pagination(self):
        # Create test data
        for i in range(15):
            Klant.objects.create(name=f'Test Klant {i}')

        request = self.factory.get(self.url)
        request.user = self.user

        response = ChoicePackage.as_view()(request)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'magazijn/pakket_kiezen.html')
        self.assertEqual(len(response.context_data['klanten_page']), 10)  # Check if only 10 items per page are displayed