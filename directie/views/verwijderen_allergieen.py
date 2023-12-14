from django.shortcuts import render, redirect
from klanten.models import Alergie
from django.shortcuts import get_object_or_404

def verwijder_allergie(request, id):
    obj = Alergie.objects.get(pk=id)
    obj.delete()
    return redirect('allergieen-overzicht')

