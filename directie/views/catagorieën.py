from django.shortcuts import render, redirect
from directie.forms import createcategorieënform
from magazijn.models import Catagorie
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required


@login_required(login_url='')
def catagorieën(request):
    catagorieën = Catagorie.objects.all()
    context = {'catagorieen': catagorieën}
    return render(request, 'directie/Categorieënoverzicht.html', context)