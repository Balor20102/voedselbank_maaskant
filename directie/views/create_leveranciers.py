# Create your views here.
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from directie.models import Leverancier
from directie.forms import createleveranciersform

def create_leveranciers(request):
    if request.method == 'POST':
        form = createleveranciersform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('directie-homepage')  # Redirect to a success page or another view
    else:
        form = createleveranciersform()

    return render(request, 'directie/leverancierstoevoegen.html', {'form': form})