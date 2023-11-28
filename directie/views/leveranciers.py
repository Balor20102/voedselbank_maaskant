# Create your views here.
from django.shortcuts import render, redirect
# from directie.forms import createcategorieënform
from django.shortcuts import get_object_or_404
from directie.models import Leverancier
from directie.forms import createleveranciersform

def leveranciers(request):
    Leveranciers = Leverancier.objects.all()
    context = {'Leverancier': Leveranciers}
    return render(request, 'directie/leveranciers.html', context)

