from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from magazijn.models import ProductItem, Pakket

from datetime import datetime


class RapportagesView(LoginRequiredMixin, View):
    
    Current_Month = datetime.now().month
    product = ProductItem
    model_pakket = Pakket
    template_name = 'directie/rapportages.html'

    def get(self, request):
        uitgaande_producten = [] # maak lege lijst aan
        inkomende_producten = self.product.objects.filter(leverings_datum__month=self.Current_Month).order_by('-leverings_datum')   # haal alle producten op die deze maand zijn geleverd
        uitgaande_pakketen = self.model_pakket.objects.filter(uitgiftdatum__month=self.Current_Month).order_by('-uitgiftdatum') # haal alle pakketten op die deze maand zijn uitgegeven

        for pakket in uitgaande_pakketen: # loop door pakketten
            uitgaande_producten.extend(self.product.objects.filter(status=2, pakket=pakket)) # voeg producten toe aan lijst

        # haal alle producten op die over datum zijn
        overdatum_producten = self.product.objects.filter(status=3, houdsbaarheiddatum__month=self.Current_Month).order_by('-leverings_datum') 

        count_inkomende_producten = len(list(inkomende_producten)) # tel aantal producten op die deze maand zijn geleverd
        count_uitgaande_producten = len(list(uitgaande_producten)) # tel aantal producten op die deze maand zijn uitgegeven
        count_overdatum_producten = len(list(overdatum_producten)) # tel aantal producten op die deze maand over datum zijn
        context = {
            'count_inkomende_producten': count_inkomende_producten,
            'count_uitgaande_producten': count_uitgaande_producten,
            'count_overdatum_producten': count_overdatum_producten,
        }

        return render(request, self.template_name, context)