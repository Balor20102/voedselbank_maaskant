
from django.views import View

from django.shortcuts import render, redirect

from django.contrib.auth.mixins import LoginRequiredMixin

from magazijn.models import Catagorie

class PCRapportage(LoginRequiredMixin, View):
    """Rapportage van de categorieën."""
    
    template_name = 'directie/product-categorie-rapportage.html'

    def get(self, request, id, *args, **kwargs):

        context = {
            'id': id
        }
        
        return render(request, self.template_name, context)