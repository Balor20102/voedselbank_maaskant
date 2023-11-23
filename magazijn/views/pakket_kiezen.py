from django.views import View

from magazijn.models import Pakket, ProductItem, Product
from klanten.models import Klant
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect

class ChoicePackage(View, LoginRequiredMixin):
    model = Pakket
    klant_model = Klant
    template_name = "magazijn/pakket_kiezen.html"

    def get(self, request):
        klant = self.klant_model.objects.all()
        context = {
            'klant': klant,
        }
        return render(request, self.template_name, context)