from django.test import TestCase, RequestFactory
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.utils import timezone

from magazijn.models import ProductItem, Product
from magazijn.views import ProductItemView


class ProductItemViewTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.url = reverse('product-item')

    def test_get(self):
        # Create test data
        product = Product.objects.create()
        product_item = ProductItem.objects.create(product=product, status=1)

        request = self.factory.get(self.url)
        request.user = self.user

        response = ProductItemView.as_view()(request, product.id)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'magazijn/product_item_overzicht.html')

        # Check if the correct product and page object are passed to the template
        self.assertEqual(response.context_data['product'], product)
        self.assertEqual(response.context_data['page_obj'], Paginator([product_item], 6).get_page(1))
        self.assertEqual(response.context_data['now'], timezone.now())