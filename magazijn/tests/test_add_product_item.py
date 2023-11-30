# tests.py
from django.test import TestCase, RequestFactory
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date

from directie.models import Leverancier
from magazijn.models import Product, Pakket, ProductItem
from magazijn.views import AddProductItem
from magazijn.forms import AddProductItemForm
from klanten.models import Klant

class AddProductItemTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.klant = Klant.objects.create(gezinsnaam='Test Gezinsnaam', volwassenen=1, kinderen=2, babies=3, postcode='1234AB', varkesvlees=True, vegataries=False, veganistisch=False)
        self.product = Product.objects.create(name='Test Product', EAN=1234567890123, voorraad=10)
        self.leverancier = Leverancier.objects.create(bedrijfsnaam='Test Leverancier', adres='Test Adres', telefoon='0612345678', leveringsdatum='2021-01-01')
        self.pakket = Pakket.objects.create(gezinsnaam=self.klant, status=2)
        self.url = reverse('product-item-add', args=[self.product.id])

    def test_post_valid_form(self):
        data = {
            'leverancier': self.leverancier.id,
            'houdsbaarheiddatum': '2021-01-01',
        }
        self.client.login(username='testuser', password='testpassword')

        # Use the Django TestCase client to perform the POST request
        response = self.client.post(self.url, data)

        # Check the HTTP status code is 302 (redirect)
        self.assertEqual(response.status_code, 302)

        # Check that the product item was created with the correct values
        product_items = ProductItem.objects.filter(product=self.product)
        self.assertTrue(product_items.exists())  # Ensure there is at least one item

        for product_item in product_items:
            self.assertEqual(product_item.leverancier, self.leverancier)
            expected_date = date(2021, 1, 1)
            self.assertEqual(product_item.houdsbaarheiddatum, expected_date)

            # Ensure that the status is set correctly based on the form data
            self.assertEqual(product_item.status, 1)
