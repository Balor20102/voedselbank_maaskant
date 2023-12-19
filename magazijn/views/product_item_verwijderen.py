from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from ..models import Product, ProductItem

class DeleteProductItem(LoginRequiredMixin, View):
    model = ProductItem


    def get(self, request, id, iditem):
        productitem = ProductItem.objects.get(id=iditem) # haal product item op
        productitem.status = 3 # zet status op verlopen
        productitem.save() # sla product item op
        product = Product.objects.get(id=id) # haal product op
        if product.voorraad > 0: # check of voorraad groter is dan 0
            product.voorraad -= 1 # haal voorraad van product af
            product.save() # sla product op
        return redirect('product-item', id=id) # redirect naar product item pagina