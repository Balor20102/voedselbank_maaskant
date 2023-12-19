from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin

class HomeView(LoginRequiredMixin, View):
    def get(self, request):
        user = request.user # haal user op
        if user.is_superuser: # check of user superuser is
            return redirect('directie-homepage') # redirect naar directie homepage
        
        if user.groups.all().count() == 0: # check of user geen groepen heeft
            return redirect('login') # redirect naar login pagina
        elif user.groups.all().count() > 1: # check of user meer dan 1 groep heeft
            return redirect('login') # redirect naar login pagina
        else:
            group = user.groups.all()[0].name # haal groep op van user
            if group == 'vrijwilliger': # check of groep vrijwilliger is
                return redirect('pakket_kiezen') # redirect naar pakket kiezen pagina
            elif group == 'medewerker': # check of groep medewerker is
                return redirect('stock-employe') # redirect naar stock pagina
            elif group == 'directie': # check of groep directie is
                return redirect('directie-homepage') # redirect naar directie homepage
            else: # als groep niet vrijwilliger, medewerker of directie is
                return redirect('login') # redirect naar login pagina