from django.test import TestCase, RequestFactory
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

from magazijn.models import Product, Pakket, ProductItem
from magazijn.views import ToevoegenPakketView


class ToevoegenPakketViewTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.url = reverse('toevoegen_pakket')

    def test_get(self):
        # Create test data
        product = Product.objects.create(name='Product 1', voorraad=10)
        pakket = Pakket.objects.create(name='Pakket 1')
        product_item = ProductItem.objects.create(product=product, status=1)

        request = self.factory.get(self.url)
        request.user = self.user

        response = ToevoegenPakketView.as_view()(request, product=product.pk, pakket=pakket.pk, hoeveel=1)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('pakket', kwargs={'pk': pakket.gezinsnaam.pk}))

        # Check if the product item is updated correctly
        updated_product_item = ProductItem.objects.get(pk=product_item.pk)
        self.assertEqual(updated_product_item.pakket, pakket)
        self.assertEqual(updated_product_item.status, 2)

        # Check if the product's stock is updated correctly
        updated_product = Product.objects.get(pk=product.pk)
        self.assertEqual(updated_product.voorraad, 9)

    def test_get_invalid_product(self):
        request = self.factory.get(self.url)
        request.user = self.user

        response = ToevoegenPakketView.as_view()(request, product=999, pakket=1, hoeveel=1)

        self.assertEqual(response.status_code, 404)
        self.assertRaises(ObjectDoesNotExist, Product.objects.get, pk=999)

    def test_get_invalid_pakket(self):
        product = Product.objects.create(name='Product 1', voorraad=10)

        request = self.factory.get(self.url)
        request.user = self.user

        response = ToevoegenPakketView.as_view()(request, product=product.pk, pakket=999, hoeveel=1)

        self.assertEqual(response.status_code, 404)
        self.assertRaises(ObjectDoesNotExist, Pakket.objects.get, pk=999)