from django.views import View
from django.shortcuts import render, redirect

from ..models import Product, ProductItem

class DeleteProductItem(View):
    model = ProductItem


    def get(self, request, id, iditem):
        productitem = ProductItem.objects.get(id=iditem)
        productitem.status = 3
        productitem.save()
        product = Product.objects.get(id=id)
        product.voorraad -= 1
        product.save()
        return redirect('product-item', id=id)