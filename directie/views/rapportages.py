from django.views import View

from django.shortcuts import render, redirect
from magazijn.models import ProductItem, Pakket

from datetime import datetime


class RapportagesView(View):
    
    Current_Month = datetime.now().month
    product = ProductItem
    model_pakket = Pakket
    template_name = 'directie/rapportages.html'

    def get(self, request):
        uitgaande_producten = []
        inkomende_producten = self.product.objects.filter(leverings_datum__month=self.Current_Month).order_by('-leverings_datum')
        uitgaande_pakketen = self.model_pakket.objects.filter(uitgiftdatum__month=self.Current_Month).order_by('-uitgiftdatum')

        for pakket in uitgaande_pakketen:
            uitgaande_producten.extend(self.product.objects.filter(status=2, pakket=pakket))

        overdatum_producten = self.product.objects.filter(status=3, houdsbaarheiddatum__month=self.Current_Month).order_by('-leverings_datum')

        count_inkomende_producten = len(list(inkomende_producten))
        count_uitgaande_producten = len(list(uitgaande_producten))
        count_overdatum_producten = len(list(overdatum_producten))
        context = {
            'count_inkomende_producten': count_inkomende_producten,
            'count_uitgaande_producten': count_uitgaande_producten,
            'count_overdatum_producten': count_overdatum_producten,
        }

        return render(request, self.template_name, context)