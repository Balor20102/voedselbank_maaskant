from django.shortcuts import render, redirect
from directie.forms import createcategorieënform
from magazijn.models import Catagorie
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required


@login_required(login_url='')
def catagorie_aanpassen(request, id):
    obj = get_object_or_404(Catagorie, id=id)
    form = createcategorieënform(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('catagorieën')
    return render(request, 'directie/Categorieënaanpassen.html', {'form': form, 'id': id})