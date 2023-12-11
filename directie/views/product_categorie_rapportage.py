# views.py
from django.views import View
from django.db.models import Count
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator

from magazijn.models import ProductItem, Product, Catagorie
from directie.filters import DateFilter


class PCRapportage(LoginRequiredMixin, View):
    product_item_model = ProductItem
    product_model = Product
    date_filter = DateFilter
    template_name = 'directie/product-categorie-rapportage.html'

    def get(self, request, *args, **kwargs):

        product_items = self.product_item_model.objects.all()

        date_filter = self.date_filter(request.GET, queryset=product_items)

        # Use the filtered queryset
        product_items = date_filter.qs

        product_counts = product_items.values('product').annotate(count=Count('product')).order_by('leverings_datum')

        for product_count in product_counts:
            product = self.product_model.objects.get(pk=product_count['product'])
            product_count['product'] = product
            

        paginated_filter = Paginator(product_counts, 10)
        page_number = request.GET.get('page')
        page_obj = paginated_filter.get_page(page_number)

        context = {
            'product_items': product_items,
            'date_filter': date_filter,
            'product_counts': page_obj,
        }

        return render(request, self.template_name, context)