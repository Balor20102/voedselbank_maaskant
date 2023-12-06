from django.views import View

from django.shortcuts import render, redirect

from django.contrib.auth.mixins import LoginRequiredMixin

from magazijn.models import Catagorie

class CategorieRapportage(LoginRequiredMixin, View):
    """Rapportage van de categorieën."""
    
    template_name = 'directie/categorie-rapportage.html'

    def get(self, request, *args, **kwargs):

        catagorieën = Catagorie.objects.all()
        context = {
            'catagorieen': catagorieën
        }
        
        return render(request, self.template_name, context)