from django.test import TestCase, RequestFactory
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta
from django.shortcuts import get_object_or_404, redirect

from magazijn.models import Pakket, Product, ProductItem
from magazijn.views import VerwijderenPakketView


class VerwijderenPakketViewTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.url = reverse('verwijderen-pakket')

    def test_get(self):
        # Create test data
        pakket = Pakket.objects.create()
        product = Product.objects.create()
        product_item = ProductItem.objects.create(pakket=pakket, product=product)

        request = self.factory.get(self.url)
        request.user = self.user

        response = VerwijderenPakketView.as_view()(request, product.id, pakket.id, 1)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('pakketten_detail', args=[pakket.id]))

        # Check if product item is updated correctly
        product_item.refresh_from_db()
        self.assertIsNone(product_item.pakket)
        self.assertEqual(product_item.status, 1)

        # Check if product is updated correctly
        product.refresh_from_db()
        self.assertEqual(product.voorraad, 1)

    def test_get_expired_product_item(self):
        # Create test data with expired product item
        pakket = Pakket.objects.create()
        product = Product.objects.create()
        expired_product_item = ProductItem.objects.create(pakket=pakket, product=product, houdsbaarheiddatum=timezone.now().date() - timedelta(days=1))

        request = self.factory.get(self.url)
        request.user = self.user

        response = VerwijderenPakketView.as_view()(request, product.id, pakket.id, 1)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('pakketten_detail', args=[pakket.id]))

        # Check if expired product item is updated correctly
        expired_product_item.refresh_from_db()
        self.assertIsNone(expired_product_item.pakket)
        self.assertEqual(expired_product_item.status, 3)

        # Check if product is not updated
        product.refresh_from_db()
        self.assertEqual(product.voorraad, 0)