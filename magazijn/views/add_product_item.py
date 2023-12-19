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
        product = Product.objects.get(id=id) # haal product op
        form = self.form_class() # maak form aan
        context = {
        'form': form,
        'product': product
        }

        return render(request, self.template_name, context) # render pagina
    
    def post(self, request, id):
        product = Product.objects.get(id=id) # haal product op

        form = self.form_class(request.POST) # maak form aan met POST data

        if form.is_valid(): # check of form valid is
            form.instance.product = product # voeg product toe aan form
            voorraad = form.cleaned_data['voorraad']    # haal voorraad op

            if voorraad != 0:  # check of voorraad niet 0 is
                product.voorraad += voorraad # voeg voorraad toe aan product
                product.save() # sla product op

                # Save the form multiple times based on 'voorraad'
                product_item = form.save(commit=False) # sla form op
                for i in range(voorraad): # loop door voorraad
                    product_item.pk = None # maak nieuwe product item aan
                    product_item.save() # sla product item op

                return redirect('product-item', id=id) # redirect naar product item pagina
            else: 
                # Redirect even if voorraad is 0
                return redirect('product-item', id=id)
            
        context = {
        'form': form,
        'product': product
        }
        return render(request, self.template_name, context) # render pagina
