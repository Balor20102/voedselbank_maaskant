from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin

from ..models import Product
from ..forms import UpdateProductForm 

class UpdateStockView(LoginRequiredMixin, View):
    model = Product
    template_name = 'magazijn/update_stock.html'
    form_class = UpdateProductForm

    def get(self, request, id):
        product = Product.objects.get(id=id) # haal product op
        form = self.form_class(instance=product) # maak form aan met product data
        context = {
            'form': form,
        }
        return render(request, self.template_name, context) # render pagina
    
    def post(self, request, id):
        form = self.form_class(request.POST, request.FILES, instance=Product.objects.get(id=id)) # maak form aan met POST data
        if form.is_valid(): # check of form valid is
            form.save() # sla form op
            return redirect('stock-employe') # redirect naar product item pagina
        context = {
            'form': form,
        }
        return render(request, self.template_name, context) # render pagina