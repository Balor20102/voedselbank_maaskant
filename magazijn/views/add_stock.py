from django.views import View
from django.shortcuts import render, redirect

from ..models import Product, Catagorie
from ..forms import ProductForm , AddProductItemForm

class AddStockView(View):
    model = Product
    template_name = 'magazijn/add_stock.html'
    form_class = ProductForm
    form_class2 = AddProductItemForm

    def get(self, request):

        context = {
        'form': self.form_class,
        'form2': self.form_class2
        }

        return render(request, self.template_name, context)
    
    def post(self, request):

        form = self.form_class(request.POST, request.FILES)
        form2 = self.form_class2(request.POST, request.FILES)

        if form.is_valid() and form2.is_valid():
            stock = form.cleaned_data['voorraad']
            product = form.save()
            
            productItem = form2.save(commit=False)
            productItem.product = product
            for x in range(stock):
                productItem.pk = None
                productItem.save()
            

            return redirect('stock-employe')

        context = {
        'form': form,
        'form2': form2
        }

        return render(request, self.template_name, context)
