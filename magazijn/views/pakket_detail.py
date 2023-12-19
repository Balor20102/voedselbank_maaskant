from django.views import View

from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.db.models import Count

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from ..filters import ProductFilter, CategorieProduct
from magazijn.models import Pakket, ProductItem, Product
from klanten.models import Klant
from magazijn.forms import UitgeefDatumForm


class PakketDetailView(LoginRequiredMixin, View):
    template_name = "magazijn/pakket-detail.html"
    pakket_model = Pakket
    product_model = Product
    product_item_model = ProductItem
    filterset_product = ProductFilter
    filterset_categorie = CategorieProduct
    form = UitgeefDatumForm

    def get(self, request, id):
        pakket = get_object_or_404(Pakket, pk=id) # haal pakket op

        klant = get_object_or_404(Klant, pk=pakket.gezinsnaam.id) # haal klant op

        product_items = self.product_item_model.objects.filter(pakket=pakket) # haal product items op
        product_counts = product_items.values('product').annotate(count=Count('product')) # haal producten op met aantal

        form = self.form(instance=pakket) # maak form aan met pakket

        context = {
            'pakket': pakket,
            'product_items': product_items,
            'product_counts': product_counts,
            'klant': klant,
            'form': form,
        }

        for product_count in product_counts: # loop door producten
            product = self.product_model.objects.get(pk=product_count['product']) # haal product op
            product_count['product'] = product # voeg product toe aan product count


        return render(request, self.template_name, context) # render pagina
    
    def post(self, request, id): # post request
        pakket = get_object_or_404(Pakket, pk=id) # haal pakket op
        form = self.form(request.POST, instance=pakket) # maak form aan met POST data
        if form.is_valid(): # check of form valid is
            pakket = form.save(commit=False) # sla form op
            pakket.save() # sla pakket op
            return redirect('pakket_kiezen') # redirect naar pakket kiezen pagina
        else: # als form niet valid is
            return redirect('pakketten_detail', id=pakket.id) # redirect naar pakket detail pagina

