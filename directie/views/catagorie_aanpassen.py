from django.shortcuts import render, redirect
from directie.forms import createcategorieënform
from magazijn.models import Catagorie
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required


@login_required(login_url='')
def catagorie_aanpassen(request, id):
    obj = get_object_or_404(Catagorie, id=id) # haal product op
    form = createcategorieënform(request.POST or None, instance=obj) # maak form aan met POST data en product data
    if form.is_valid(): # check of form valid is
        form.save() # sla form op
        return redirect('catagorieën') # redirect naar product item pagina
    return render(request, 'directie/Categorieënaanpassen.html', {'form': form, 'id': id})