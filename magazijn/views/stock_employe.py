from django.shortcuts import render
from django.core.paginator import Paginator
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

from ..models import Product

from ..filters import ProductFilter, CategorieProduct

class StockEmployeView(LoginRequiredMixin, View):
    model = Product
    filterset_product = ProductFilter
    filterset_categorie = CategorieProduct
    template_name = 'magazijn/stock-employe.html'

    def get(self, request):
        sq_filters = self.filterset_product(request.GET, queryset=self.model.objects.all()) # filter producten
        sq_filters2 = self.filterset_categorie(request.GET, queryset=sq_filters.qs) # filter producten op categorie
        paginated_filter = Paginator(sq_filters2.qs, 10) # maak pagina's aan
        page_number = request.GET.get('page') # haal pagina nummer op
        page_obj = paginated_filter.get_page(page_number) # haal pagina op

        context = {
            'filter': sq_filters,
            'filter2': sq_filters2,
            'page_obj': page_obj,
        }

        return render(request, self.template_name, context ) # render pagina

