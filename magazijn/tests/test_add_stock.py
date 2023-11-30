from django.test import TestCase, RequestFactory
from django.urls import reverse
from django.contrib.auth.models import User

from magazijn.models import Product
from magazijn.views import AddStockView
from magazijn.forms import ProductForm, AddProductItemForm


class AddStockViewTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.url = reverse('add-stock')

    def test_get(self):
        request = self.factory.get(self.url)
        request.user = self.user

        response = AddStockView.as_view()(request)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'magazijn/add_stock.html')
        self.assertIsInstance(response.context_data['form'], ProductForm)
        self.assertIsInstance(response.context_data['form2'], AddProductItemForm)

    def test_post_valid_form(self):
        data = {
            'voorraad': 5,
            # Include other required fields for the ProductForm and AddProductItemForm
        }
        request = self.factory.post(self.url, data)
        request.user = self.user

        response = AddStockView.as_view()(request)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('stock-employe'))

        # Add assertions to check if the product and product items are created correctly

    def test_post_invalid_form(self):
        data = {
            'voorraad': -5,  # Invalid stock value
            # Include other required fields for the ProductForm and AddProductItemForm
        }
        request = self.factory.post(self.url, data)
        request.user = self.user

        response = AddStockView.as_view()(request)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'magazijn/add_stock.html')
        self.assertIsInstance(response.context_data['form'], ProductForm)
        self.assertIsInstance(response.context_data['form2'], AddProductItemForm)
        self.assertFormError(response, 'form', 'voorraad', 'Ensure this value is greater than or equal to 0')