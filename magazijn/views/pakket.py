from django.views import View

from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator

from ..filters import ProductFilter, CategorieProduct
from magazijn.models import Pakket, ProductItem, Product
from klanten.models import Klant



class PakketView(LoginRequiredMixin, View):
    template_name = "magazijn/pakketten.html"
    pakket_model = Pakket
    product_model = Product
    product_item_model = ProductItem
    filterset_product = ProductFilter
    filterset_categorie = CategorieProduct



    def get(self, request, pk):
        
        klant = get_object_or_404(Klant, pk=pk) # haal klant op
        pakket = self.pakket_model.objects.get_or_create(gezinsnaam=klant, aangemaakt_op= timezone.now()) # maak pakket aan

        product = self.product_model.objects.filter(voorraad__gt=0) # haal producten op met voorraad
        sq_filters = self.filterset_product(request.GET, queryset=product) # filter producten
        sq_filters2 = self.filterset_categorie(request.GET, queryset=sq_filters.qs) # filter producten op categorie
        paginated_filter = Paginator(sq_filters2.qs, 10) # maak pagina's aan
        page_number = request.GET.get('page') # haal pagina nummer op
        page_obj = paginated_filter.get_page(page_number) # haal pagina op

        context = {
            'filter': sq_filters,
            'filter2': sq_filters2,
            'page_obj': page_obj,
            'pakket': pakket,
        } 

        return render(request, self.template_name, context ) # render pagina
