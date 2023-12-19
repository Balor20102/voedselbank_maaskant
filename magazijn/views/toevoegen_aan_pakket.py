from django.views import View

from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator

from ..filters import ProductFilter, CategorieProduct
from magazijn.models import Pakket, ProductItem, Product
from klanten.models import Klant

class ToevoegenPakketView(LoginRequiredMixin, View):
    pakket_model = Pakket
    product_model = Product
    product_item_model = ProductItem
    filterset_product = ProductFilter
    filterset_categorie = CategorieProduct

    def get(self, request, product, pakket, hoeveel): # get request
        product = get_object_or_404(Product, pk=product) # haal product op
        pakket = get_object_or_404(Pakket, pk=pakket) # haal pakket op
        # haal product items op met status 1 (beschikbaar) en sorteer op houdbaarheidsdatum
        product_items = self.product_item_model.objects.filter(product=product, status = 1).order_by('houdsbaarheiddatum') 
        for i, item in zip(range(hoeveel), product_items): # loop door product items
                item.pakket = pakket # voeg pakket toe aan product item
                item.status = 2 # zet status op uitgegeven
                item.save() # sla product item op

        product.voorraad -= hoeveel # haal voorraad van product af
        product.save() # sla product op
        return redirect('pakket', pk=pakket.gezinsnaam.pk) # redirect naar pakket pagina