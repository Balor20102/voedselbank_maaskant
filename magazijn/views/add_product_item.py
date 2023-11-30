from django.views import View
from django.shortcuts import render, redirect

from ..models import Product, ProductItem
from ..forms import ProductForm , AddProductItemForm

class AddProductItem(View):
    model = ProductItem
    template_name = 'magazijn/add_product_item.html'
    form_class = AddProductItemForm

    def get(self, request, id):
        product = Product.objects.get(id=id)
        form = self.form_class()
        context = {
        'form': form,
        'product': product
        }

        return render(request, self.template_name, context)
    
    def post(self, request, id):
        product = Product.objects.get(id=id)

        form = self.form_class(request.POST)

        if form.is_valid():
            form.save(commit=False)
            form.instance.product = product
            form.save()
            return redirect('product-item', id=id)
        
        context = {
        'form': form,
        'product': product
        }
        return render(request, self.template_name, context)
