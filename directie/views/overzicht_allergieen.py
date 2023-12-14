from django.shortcuts import render, redirect
from directie.forms import createcategorieënform
from klanten.models import Alergie
from django.shortcuts import get_object_or_404


def alergie(request):
    allergieen = Alergie.objects.all()
    context = {'allergieen': allergieen}
    return render(request, 'directie/alergieoverzicht.html', context)