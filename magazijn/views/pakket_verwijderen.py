from django.views import View

from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator

from ..filters import ProductFilter, CategorieProduct
from magazijn.models import Pakket, ProductItem, Product
from klanten.models import Klant

class VerwijderenPakketView(LoginRequiredMixin, View):
    pakket_model = Pakket
    product_model = Product
    product_item_model = ProductItem
    filterset_product = ProductFilter
    filterset_categorie = CategorieProduct

    def get(self, request, product, pakket, hoeveel):
        pakket = get_object_or_404(Pakket, pk=pakket)
        product = get_object_or_404(Product, pk=product)
        product_item = ProductItem.objects.filter(pakket=pakket, product=product).order_by('-houdsbaarheiddatum')
        for i , product_item in zip(range(hoeveel) , product_item):
            if product_item.houdsbaarheiddatum < timezone.now().date():
                product_item.status = 3
                product_item.pakket = None
                product_item.save()
            else:
                product_item.pakket = None
                product_item.status = 1
                product_item.save()
                product.voorraad = product.voorraad + 1
                product.save()
        return redirect('pakketten_detail', id=pakket.id)