from django.test import TestCase, RequestFactory
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

from magazijn.models import Product, ProductItem
from magazijn.views import UpdateProductItem


class UpdateProductItemViewTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.url = reverse('update-product-item', kwargs={'id': 1, 'iditem': 1})

    def test_get(self):
        # Create test data
        product = Product.objects.create(name='Product 1', voorraad=10)
        product_item = ProductItem.objects.create(product=product, status=1)

        request = self.factory.get(self.url)
        request.user = self.user

        response = UpdateProductItem.as_view()(request, id=product.pk, iditem=product_item.pk)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'magazijn/add_product_item.html')
        self.assertEqual(response.context_data['product'], product)
        self.assertEqual(response.context_data['productitem'], product_item)

    def test_post_valid_form(self):
        # Create test data
        product = Product.objects.create(name='Product 1', voorraad=10)
        product_item = ProductItem.objects.create(product=product, status=1)

        request = self.factory.post(self.url, data={'some_field': 'some_value'})
        request.user = self.user

        response = UpdateProductItem.as_view()(request, id=product.pk, iditem=product_item.pk)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('product-item', kwargs={'id': product.pk}))

        # Check if the form is saved correctly
        updated_product_item = ProductItem.objects.get(pk=product_item.pk)
        self.assertEqual(updated_product_item.product, product)
        self.assertEqual(updated_product_item.some_field, 'some_value')

    def test_post_invalid_form(self):
        # Create test data
        product = Product.objects.create(name='Product 1', voorraad=10)
        product_item = ProductItem.objects.create(product=product, status=1)

        request = self.factory.post(self.url, data={})
        request.user = self.user

        response = UpdateProductItem.as_view()(request, id=product.pk, iditem=product_item.pk)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'magazijn/add_product_item.html')
        self.assertEqual(response.context_data['product'], product)
        self.assertEqual(response.context_data['productitem'], product_item)
        self.assertFormError(response, 'form', 'some_field', 'This field is required.')