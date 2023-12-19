from django.views import View
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin

from django.core.paginator import Paginator

from django.utils import timezone

from magazijn.models import Product, ProductItem

class ProductItemView(LoginRequiredMixin, View):

    template_name = 'magazijn/product_item_overzicht.html'
    model = ProductItem
    model2 = Product
    paginate_by = 6

    def get(self, request, id, *args, **kwargs):
        productitem = ProductItem.objects.filter(product__id=id, status = 1).order_by('houdsbaarheiddatum') # haal product items op
        product = Product.objects.get(id=id) # haal product op
        paginator = Paginator(productitem, self.paginate_by) # maak pagina's aan    
        page_number = request.GET.get('page') # haal pagina nummer op
        page_obj = paginator.get_page(page_number) # haal pagina op
        context = {
            'product': product,
            'page_obj': page_obj,
            'now': timezone.now(), # haal huidige tijd op
        }

        return render(request, self.template_name, context) # render pagina
    
        
