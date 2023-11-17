from django.shortcuts import render, redirect
from directie.forms import createcategorieënform
from magazijn.models import Catagorie
from django.shortcuts import get_object_or_404

def verwijder_catagorie(request, char_field_value):
    obj = get_object_or_404(Catagorie, char_field=char_field_value)
    obj.delete()
    catagorieën = Catagorie.objects.all()
    context = {'catagorieen': catagorieën}
    return render(request, 'directie/Categorieënoverzicht.html', context)