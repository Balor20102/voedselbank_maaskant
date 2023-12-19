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
        pakket = get_object_or_404(Pakket, pk=pakket) # haal pakket op
        product = get_object_or_404(Product, pk=product) # haal product op
        product_item = ProductItem.objects.filter(pakket=pakket, product=product).order_by('-houdsbaarheiddatum') # haal product items op
        for i , product_item in zip(range(hoeveel) , product_item): # loop door product items
            if product_item.houdsbaarheiddatum < timezone.now().date(): # check of houdbaarheidsdatum verlopen is
                product_item.status = 3     # zet status op verlopen
                product_item.pakket = None # zet pakket op None
                product_item.save() # sla product item op
            else:
                product_item.pakket = None # zet pakket op None
                product_item.status = 1 # zet status op beschikbaar
                product_item.save() # sla product item op
                product.voorraad = product.voorraad + 1     # voeg voorraad toe aan product
                product.save() # sla product op
        return redirect('pakketten_detail', id=pakket.id) # redirect naar pakket detail pagina