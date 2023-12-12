from django.shortcuts import render
from klanten.models import Klant
from directie.models import Leverancier

def directiehomepage(request):
    klanten = Klant.objects.all()
    leveranciers = Leverancier.objects.all()
    klanten_aantal = klanten.count()
    leveranciers_aantal = leveranciers.count()
    context = {"leveranciers": leveranciers_aantal, "klanten": klanten_aantal}
    return render(request, 'directie/homepagina.html', context)