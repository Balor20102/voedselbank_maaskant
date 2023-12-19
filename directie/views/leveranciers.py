# Create your views here.
from django.shortcuts import render, redirect
# from directie.forms import createcategorieënform
from django.shortcuts import get_object_or_404
from directie.models import Leverancier
from directie.forms import createleveranciersform
from django.contrib.auth.decorators import login_required


@login_required(login_url='')
def leveranciers(request):
    Leveranciers = Leverancier.objects.all()
    context = {'Leveranciers': Leveranciers}
    # raise ValueError(context)
    return render(request, 'directie/leveranciers.html', context)


@login_required(login_url='')
def verwijder_leveranciers(request, id):
    obj = Leverancier.objects.get(pk=id)
    obj.delete()
    return redirect('directie-homepage')


@login_required(login_url='')
def create_leveranciers(request):
    if request.method == 'POST':
        form = createleveranciersform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('directie-homepage')  # Redirect to a success page or another view
    else:
        form = createleveranciersform()

    return render(request, 'directie/leverancierstoevoegen.html', {'form': form})

@login_required(login_url='')
def leveranciers_aanpassen(request, id):
    obj = get_object_or_404(Leverancier, id=id) # haal product op
    form = createleveranciersform(request.POST or None, instance=obj) # maak form aan met POST data en product data
    if form.is_valid(): # check of form valid is
        form.save() # sla form op
        return redirect('directie-homepage') # redirect naar product item pagina
    return render(request, 'directie/leverancieraanpassen.html', {'form': form, 'id': id}) 