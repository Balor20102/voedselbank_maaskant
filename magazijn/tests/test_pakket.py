from django.test import TestCase, RequestFactory
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta
from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator

from magazijn.models import Pakket, Product, ProductItem
from klanten.models import Klant
from magazijn.views import PakketView
from magazijn.filters import ProductFilter, CategorieProduct


class PakketViewTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.url = reverse('pakket-view')

    def test_get(self):
        # Create test data
        klant = Klant.objects.create()
        pakket = Pakket.objects.create(gezinsnaam=klant, aangemaakt_op=timezone.now())
        product = Product.objects.create(voorraad=1)
        product_item = ProductItem.objects.create(pakket=pakket, product=product)
        request = self.factory.get(self.url)
        request.user = self.user

        response = PakketView.as_view()(request, klant.id)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.template_name, "magazijn/pakketten.html")

        # Check if context variables are passed correctly
        context = response.context_data
        self.assertEqual(context['pakket'], pakket)
        self.assertEqual(context['page_obj'], Paginator([product_item], 10).get_page(1))

    def test_get_no_products(self):
        # Create test data with no available products
        klant = Klant.objects.create()
        pakket = Pakket.objects.create(gezinsnaam=klant, aangemaakt_op=timezone.now())
        request = self.factory.get(self.url)
        request.user = self.user

        response = PakketView.as_view()(request, klant.id)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.template_name, "magazijn/pakketten.html")

        # Check if context variables are passed correctly
        context = response.context_data
        self.assertEqual(context['pakket'], pakket)
        self.assertEqual(context['page_obj'], Paginator([], 10).get_page(1))