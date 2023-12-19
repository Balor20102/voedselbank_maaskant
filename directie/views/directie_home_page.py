from django.shortcuts import render
from klanten.models import Klant
from directie.models import Leverancier
from django.contrib.auth.decorators import login_required


@login_required(login_url='')
def directiehomepage(request):
    klanten = Klant.objects.all() # haal alle producten op
    leveranciers = Leverancier.objects.all() # haal alle producten op
    klanten_aantal = klanten.count() # tel aantal producten
    leveranciers_aantal = leveranciers.count() # tel aantal producten
    context = {"leveranciers": leveranciers_aantal, "klanten": klanten_aantal}
    return render(request, 'directie/homepagina.html', context)