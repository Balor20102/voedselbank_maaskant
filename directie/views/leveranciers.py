# Create your views here.
from django.shortcuts import render, redirect
# from directie.forms import createcategorieënform
from django.shortcuts import get_object_or_404
from directie.models import Leverancier
from directie.forms import createleveranciersform

def leveranciers(request):
    Leveranciers = Leverancier.objects.all()
    context = {'Leveranciers': Leveranciers}
    # raise ValueError(context)
    return render(request, 'directie/leveranciers.html', context)

def verwijder_leveranciers(request, id):
    obj = Leverancier.objects.get(pk=id)
    obj.delete()
    return redirect('directie-homepage')

def create_leveranciers(request):
    if request.method == 'POST':
        form = createleveranciersform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('directie-homepage')  # Redirect to a success page or another view
    else:
        form = createleveranciersform()

    return render(request, 'directie/leverancierstoevoegen.html', {'form': form})

def leveranciers_aanpassen(request, id):
    obj = get_object_or_404(Leverancier, id=id)
    form = createleveranciersform(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('directie-homepage')
    return render(request, 'directie/leverancieraanpassen.html', {'form': form, 'id': id})