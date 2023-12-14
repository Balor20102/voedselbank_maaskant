from django.shortcuts import render, redirect
from klanten.models import Alergie
from django.shortcuts import get_object_or_404
from directie.forms import createAlergieform

def allergieen_aanpassen(request, id):
    obj = get_object_or_404(Alergie, id=id)
    form = createAlergieform(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('allergieen-overzicht')
    return render(request, 'directie/allergieenaanpassen.html', {'form': form, 'id': id})