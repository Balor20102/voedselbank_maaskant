from django.test import TestCase, RequestFactory
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

from magazijn.models import Product
from magazijn.forms import ProductForm
from magazijn.views import UpdateStockView


class UpdateStockViewTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.url = reverse('update-stock', kwargs={'id': 1})

    def test_get(self):
        # Create test data
        product = Product.objects.create(name='Product 1', voorraad=10)

        request = self.factory.get(self.url)
        request.user = self.user

        response = UpdateStockView.as_view()(request, id=product.pk)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'magazijn/update_stock.html')
        self.assertEqual(response.context_data['form'].instance, product)

    def test_post_valid_form(self):
        # Create test data
        product = Product.objects.create(name='Product 1', voorraad=10)

        request = self.factory.post(self.url, data={'name': 'Updated Product', 'voorraad': 20})
        request.user = self.user

        response = UpdateStockView.as_view()(request, id=product.pk)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('stock-employe'))

        # Check if the form is saved correctly
        updated_product = Product.objects.get(pk=product.pk)
        self.assertEqual(updated_product.name, 'Updated Product')
        self.assertEqual(updated_product.voorraad, 20)

    def test_post_invalid_form(self):
        # Create test data
        product = Product.objects.create(name='Product 1', voorraad=10)

        request = self.factory.post(self.url, data={})
        request.user = self.user

        response = UpdateStockView.as_view()(request, id=product.pk)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'magazijn/update_stock.html')
        self.assertEqual(response.context_data['form'].instance, product)
        self.assertFormError(response, 'form', 'name', 'This field is required.')