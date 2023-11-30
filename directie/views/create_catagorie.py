# Create your views here.
from django.shortcuts import render, redirect
from directie.forms import createcategorieënform
from django.shortcuts import get_object_or_404

def create_catagorie(request):
    if request.method == 'POST':
        form = createcategorieënform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('directie-homepage')  # Redirect to a success page or another view
    else:
        form = createcategorieënform()

    return render(request, 'directie/Categorieëtoevoegen.html', {'form': form})