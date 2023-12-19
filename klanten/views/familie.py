from klanten.models import Klant
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from directie.forms import createleveranciersform, klantenaanpassenform

@login_required(login_url='')
def klanten(request): 
    Klanten = Klant.objects.all() # haal alle klanten op
    context = {'Klanten': Klanten} # sla klanten op in context
    return render(request, 'klanten/klanten.html', context)

@login_required(login_url='')
def verwijder_klanten(request, id): 
    obj = Klant.objects.get(pk=id) # haal klant op
    obj.delete() # verwijder klant
    return redirect('directie-homepage')

@login_required(login_url='')
def create_klanten(request):
    if request.method == 'POST': # check of request een POST request is
        form = klantenaanpassenform(request.POST) # maak form aan met POST data
        if form.is_valid(): # check of form valid is
            form.save() # sla form op
            return redirect('directie-homepage')  # Redirect to a success page or another view
    else:
        form = klantenaanpassenform() # maak form aan

    return render(request, 'klanten/familietoevoegen.html', {'form': form})

@login_required(login_url='')
def klanten_aanpassen(request, id):
    obj = get_object_or_404(Klant, id=id) # haal klant op
    form = klantenaanpassenform(request.POST or None, instance=obj) # maak form aan met POST data
    if form.is_valid(): # check of form valid is
        form.save() # sla form op
        return redirect('directie-homepage')
    return render(request, 'klanten/familieaanpassen.html', {'form': form, 'id': id})