from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator

from magazijn.models import Catagorie

class CategorieRapportage(LoginRequiredMixin, View):
    """Rapportage van de categorieën."""
    
    template_name = 'directie/categorie-rapportage.html'

    def get(self, request, *args, **kwargs):

        catagorieën = Catagorie.objects.all()
        paginator = Paginator(catagorieën, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context = {
            'page_obj': page_obj
        }
        
        return render(request, self.template_name, context)