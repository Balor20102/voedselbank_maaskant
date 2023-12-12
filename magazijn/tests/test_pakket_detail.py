from django.test import TestCase, RequestFactory
from django.urls import reverse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
from django.db.models import Count

from magazijn.models import Pakket, Product, ProductItem
from klanten.models import Klant
from magazijn.views import PakketDetailView
from magazijn.forms import UitgeefDatumForm

class PakketDetailViewTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.pakket = Pakket.objects.create(name='Test Pakket')
        self.url = reverse('pakket-detail', args=[self.pakket.id])

    def test_get(self):
        request = self.factory.get(self.url)
        request.user = self.user

        response = PakketDetailView.as_view()(request, id=self.pakket.id)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'magazijn/pakket-detail.html')
        self.assertIsInstance(response.context_data['form'], UitgeefDatumForm)
        self.assertEqual(response.context_data['pakket'], self.pakket)

    def test_post_valid_form(self):
        data = {
            # Add valid form data here
        }
        request = self.factory.post(self.url, data)
        request.user = self.user

        response = PakketDetailView.as_view()(request, id=self.pakket.id)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('pakket_kiezen'))

        pakket = get_object_or_404(Pakket, pk=self.pakket.id)
        # Add assertions for the updated pakket object here

    def test_post_invalid_form(self):
        data = {
            # Add invalid form data here
        }
        request = self.factory.post(self.url, data)
        request.user = self.user

        response = PakketDetailView.as_view()(request, id=self.pakket.id)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('pakketten_detail', args=[self.pakket.id]))