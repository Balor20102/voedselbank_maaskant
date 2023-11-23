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
        klant = get_object_or_404(Klant, pk=pk)
        pakket = self.pakket_model.objects.get_or_create(gezinsnaam=klant, aangemaakt_op= timezone.now())

        product = self.product_model.objects.filter(voorraad__gt=0)
        sq_filters = self.filterset_product(request.GET, queryset=product)
        sq_filters2 = self.filterset_categorie(request.GET, queryset=sq_filters.qs)
        paginated_filter = Paginator(sq_filters2.qs, 10)
        page_number = request.GET.get('page')
        page_obj = paginated_filter.get_page(page_number)

        context = {
            'filter': sq_filters,
            'filter2': sq_filters2,
            'page_obj': page_obj,
            'pakket': pakket,
        }

        return render(request, self.template_name, context )
