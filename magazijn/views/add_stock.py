from django.views import View
from django.shortcuts import render

from ..models import Product, Catagorie
from ..forms import ProductForm 

class AddStockView(View):
    model = Product
    template_name = 'magazijn/add_stock.html'
    form_class = ProductForm

    def get(self, request):
        return render(request, self.template_name, {'form': self.form_class})
