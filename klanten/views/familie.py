from klanten.models import Klant
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from directie.forms import createleveranciersform, klantenaanpassenform

def klanten(request):
    Klanten = Klant.objects.all()
    context = {'Klanten': Klanten}
    return render(request, 'klanten/klanten.html', context)

def verwijder_klanten(request, id):
    obj = Klant.objects.get(pk=id)
    obj.delete()
    return redirect('directie-homepage')

def create_klanten(request):
    if request.method == 'POST':
        form = klantenaanpassenform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('directie-homepage')  # Redirect to a success page or another view
    else:
        form = klantenaanpassenform()

    return render(request, 'klanten/familietoevoegen.html', {'form': form})

def klanten_aanpassen(request, id):
    obj = get_object_or_404(Klant, id=id)
    form = klantenaanpassenform(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('directie-homepage')
    return render(request, 'klanten/familieaanpassen.html', {'form': form, 'id': id})