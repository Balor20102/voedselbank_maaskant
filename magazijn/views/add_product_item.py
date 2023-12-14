from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from ..models import Product, ProductItem
from ..forms import ProductForm , AddProductItemForm

class AddProductItem(LoginRequiredMixin, View):
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
            form.instance.product = product
            voorraad = form.cleaned_data['voorraad']

            if voorraad != 0:
                product.voorraad += voorraad
                product.save()

                # Save the form multiple times based on 'voorraad'
                product_item = form.save(commit=False)
                for i in range(voorraad):
                    product_item.pk = None
                    product_item.save()

                return redirect('product-item', id=id)
            else:
                # Redirect even if voorraad is 0
                return redirect('product-item', id=id)
            
        context = {
        'form': form,
        'product': product
        }
        return render(request, self.template_name, context)
