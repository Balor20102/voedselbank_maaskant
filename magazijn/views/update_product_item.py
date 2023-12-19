from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from ..models import Product, ProductItem
from ..forms import ProductForm , updateProductItemForm

class UpdateProductItem(LoginRequiredMixin, View):
    model = ProductItem
    template_name = 'magazijn/add_product_item.html'
    form_class = updateProductItemForm

    def get(self, request, id, iditem): 
        product = Product.objects.get(id=id) # haal product op
        productitem = ProductItem.objects.get(id=iditem) # haal product item op
        form = self.form_class(instance=productitem) # maak form aan met product item data
        context = { 
        'form': form,
        'product': product,
        'productitem': productitem
        }

        return render(request, self.template_name, context) # render pagina
    
    def post(self, request, id, iditem):
        product = Product.objects.get(id=id) # haal product op
        productitem = ProductItem.objects.get(id=iditem) # haal product item op

        form = self.form_class(request.POST, instance=productitem) # maak form aan met POST data
        

        if form.is_valid(): # check of form valid is
            status = int(form.cleaned_data['status']) # haal status op
            form.save(commit=False) # sla form op
            if status != 1: # check of status niet 1 is
                product.voorraad -= 1 # haal voorraad van product af
                productitem.status = status # zet status op form
                productitem.save() # sla product item op
                product.save() # sla product op
            
            form.instance.status = status # zet status op form
            form.instance.product = product # voeg product toe aan form
            form.save() # sla form op
            return redirect('product-item', id=id) # redirect naar product item pagina
        
        context = {
        'form': form,
        'product': product,
        'productitem': productitem
        }
        render(request, self.template_name, context) # render pagina
