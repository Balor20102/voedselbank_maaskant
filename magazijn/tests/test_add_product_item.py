from django.test import TestCase, RequestFactory
from django.urls import reverse
from django.contrib.auth.models import User

from magazijn.models import Product, ProductItem
from magazijn.views import AddProductItem
from magazijn.forms import AddProductItemForm


class AddProductItemTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.product = Product.objects.create(name='Test Product', price=10.0)
        self.url = reverse('add-product-item', args=[self.product.id])

    def test_get(self):
        request = self.factory.get(self.url)
        request.user = self.user

        response = AddProductItem.as_view()(request, id=self.product.id)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'magazijn/add_product_item.html')
        self.assertIsInstance(response.context_data['form'], AddProductItemForm)
        self.assertEqual(response.context_data['product'], self.product)

    def test_post_valid_form(self):
        data = {
            'quantity': 5,
        }
        request = self.factory.post(self.url, data)
        request.user = self.user

        response = AddProductItem.as_view()(request, id=self.product.id)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('product-item', args=[self.product.id]))

        product_item = ProductItem.objects.get(product=self.product)
        self.assertEqual(product_item.quantity, data['quantity'])

    def test_post_invalid_form(self):
        data = {
            'quantity': -5,  # Invalid quantity
        }
        request = self.factory.post(self.url, data)
        request.user = self.user

        response = AddProductItem.as_view()(request, id=self.product.id)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'magazijn/add_product_item.html')
        self.assertIsInstance(response.context_data['form'], AddProductItemForm)
        self.assertEqual(response.context_data['product'], self.product)
        self.assertFormError(response, 'form', 'quantity', 'Ensure this value is greater than or equal to 0')
 