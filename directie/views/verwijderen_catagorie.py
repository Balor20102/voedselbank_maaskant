from django.shortcuts import render, redirect
from directie.forms import createcategorieënform
from magazijn.models import Catagorie
from django.shortcuts import get_object_or_404

def verwijder_catagorie(request, id):
    obj = Catagorie.objects.get(pk=id)
    obj.delete()
    return redirect('catagorieën')

