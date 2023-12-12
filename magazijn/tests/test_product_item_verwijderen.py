from django.test import TestCase, RequestFactory
from django.urls import reverse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect

from magazijn.models import ProductItem, Product
from magazijn.views import DeleteProductItem


class DeleteProductItemViewTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.url = reverse('product-item')

    def test_get(self):
        # Create test data
        product = Product.objects.create()
        product_item = ProductItem.objects.create(product=product)

        request = self.factory.get(self.url)
        request.user = self.user

        response = DeleteProductItem.as_view()(request, product.id, product_item.id)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('product-item', args=[product.id]))

        # Check if product item is updated correctly
        product_item.refresh_from_db()
        self.assertEqual(product_item.status, 3)

        # Check if product is updated correctly
        product.refresh_from_db()
        self.assertEqual(product.voorraad, 0)