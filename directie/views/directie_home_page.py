from django.shortcuts import render, redirect
from directie.forms import createcategorieënform
from django.shortcuts import get_object_or_404

def directiehomepage(request):
    return render(request, 'directie/homepagina.html')