from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin

class HomeView(LoginRequiredMixin, View):
    def get(self, request):
        user = request.user
        if user.is_superuser:
            return redirect('directie-homepage')
        
        if user.groups.all().count() == 0:
            return redirect('login')
        elif user.groups.all().count() > 1:
            return redirect('login')
        else:
            group = user.groups.all()[0].name
            if group == 'vrijwilliger':
                return redirect('pakket_kiezen')
            elif group == 'medewerker':
                return redirect('stock-employe')
            elif group == 'directie':
                return redirect('directie-homepage')
            else:
                return redirect('login')