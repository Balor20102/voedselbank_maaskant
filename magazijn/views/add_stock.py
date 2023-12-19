from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from ..models import Product, Catagorie
from ..forms import ProductForm , StockAddProductItemForm

class AddStockView(LoginRequiredMixin,View):
    model = Product
    template_name = 'magazijn/add_stock.html'
    form_class = ProductForm
    form_class2 = StockAddProductItemForm

    def get(self, request):

        context = {
        'form': self.form_class,
        'form2': self.form_class2
        }

        return render(request, self.template_name, context) 
    
    def post(self, request):

        form = self.form_class(request.POST, request.FILES) # maak form aan met POST data
        form2 = self.form_class2(request.POST, request.FILES) # maak form aan met POST data

        if form.is_valid() and form2.is_valid(): # check of form valid is en form2
            stock = form.cleaned_data['voorraad']   # haal voorraad op
            if stock <= 0: # check of voorraad niet 0 is
                stock = 0 # zet voorraad op 0
            product = form.save(commit=False) # sla form op
            product.voorraad = stock # voeg voorraad toe aan product
            product.save() # sla product op
            
            productItem = form2.save(commit=False) # sla form2 op
            productItem.product = product # voeg product toe aan form2
            if stock <= 0: # check of voorraad niet 0 is
                stock = 0 # zet voorraad op 0

            for x in range(stock): # loop door voorraad
                productItem.pk = None # maak nieuwe product item aan
                productItem.save()  # sla product item op
            

            return redirect('stock-employe') # redirect naar product item pagina

        context = {
        'form': form,
        'form2': form2
        }

        return render(request, self.template_name, context) # render pagina
