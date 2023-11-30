from django.test import TestCase, RequestFactory
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.paginator import Paginator

from magazijn.models import Product
from magazijn.views import StockEmployeView


class StockEmployeViewTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.url = reverse('stock-employe')

    def test_get(self):
        # Create test data
        product1 = Product.objects.create(name='Product 1')
        product2 = Product.objects.create(name='Product 2')

        request = self.factory.get(self.url)
        request.user = self.user

        response = StockEmployeView.as_view()(request)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'magazijn/stock-employe.html')

        # Check if the correct filters and page object are passed to the template
        self.assertEqual(response.context_data['filter'].qs.count(), 2)
        self.assertEqual(response.context_data['filter2'].qs.count(), 2)
        self.assertEqual(response.context_data['page_obj'], Paginator(response.context_data['filter2'].qs, 10).get_page(1))