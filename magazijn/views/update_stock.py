from django.views import View
from django.shortcuts import render, redirect

from ..models import Product
from ..forms import ProductForm 

class UpdateStockView(View):
    model = Product
    template_name = 'magazijn/update_stock.html'
    form_class = ProductForm

    def get(self, request, id):

        product = Product.objects.get(id=id)
        form = self.form_class(instance=product)

        context = {
        'form': form,
        }

        return render(request, self.template_name, context)
    
    def post(self, request, id):
        form = self.form_class(request.POST, request.FILES, instance=Product.objects.get(id=id))
        if form.is_valid():
            form.save()
            
            return redirect('stock-employe')
        

        context = {
        'form': form,
        }

        return render(request, self.template_name, context)