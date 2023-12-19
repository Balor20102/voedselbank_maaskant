from django.shortcuts import render, redirect
from klanten.models import Alergie
from django.shortcuts import get_object_or_404
from directie.forms import createAlergieform
from django.contrib.auth.decorators import login_required


@login_required(login_url='')
def allergieen_aanpassen(request, id):
    obj = get_object_or_404(Alergie, id=id) # haal product op
    form = createAlergieform(request.POST or None, instance=obj) # maak form aan met POST data en product data 
    if form.is_valid(): # check of form valid is
        form.save() # sla form op
        return redirect('allergieen-overzicht')
    return render(request, 'directie/allergieenaanpassen.html', {'form': form, 'id': id})