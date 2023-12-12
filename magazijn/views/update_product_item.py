from django.views import View
from django.shortcuts import render, redirect

from ..models import Product, ProductItem
from ..forms import ProductForm , updateProductItemForm

class UpdateProductItem(View):
    model = ProductItem
    template_name = 'magazijn/add_product_item.html'
    form_class = updateProductItemForm

    def get(self, request, id, iditem):
        product = Product.objects.get(id=id)
        productitem = ProductItem.objects.get(id=iditem)
        form = self.form_class(instance=productitem)
        context = {
        'form': form,
        'product': product,
        'productitem': productitem
        }

        return render(request, self.template_name, context)
    
    def post(self, request, id, iditem):
        product = Product.objects.get(id=id)
        productitem = ProductItem.objects.get(id=iditem)

        form = self.form_class(request.POST, instance=productitem)
        

        if form.is_valid():
            status = int(form.cleaned_data['status'])
            form.save(commit=False)
            if status != 1:
                product.voorraad -= 1
                productitem.status = status
                productitem.save()
                product.save()
            
            form.instance.status = status
            form.instance.product = product
            form.save()
            return redirect('product-item', id=id)
        
        context = {
        'form': form,
        'product': product,
        'productitem': productitem
        }
        render(request, self.template_name, context)
