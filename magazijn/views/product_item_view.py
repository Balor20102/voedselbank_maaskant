from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator
from django.urls import reverse
from django.http import HttpResponseRedirect

from magazijn.models import Product, ProductItem

class ProductItemView(LoginRequiredMixin, View):

    template_name = 'magazijn/product_item_overzicht.html'
    model = ProductItem
    model2 = Product
    paginate_by = 6

    def get(self, request, id, *args, **kwargs):
        productitem = ProductItem.objects.filter(product__id=id).order_by('houdsbaarheiddatum')
        product = Product.objects.get(id=id)
        paginator = Paginator(productitem, self.paginate_by)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {
            'product': product,
            'page_obj': page_obj,
        }

        return render(request, self.template_name, context)
    
        
