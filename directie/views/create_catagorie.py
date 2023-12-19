# Create your views here.
from django.shortcuts import render, redirect
from directie.forms import createcategorieënform
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required


@login_required(login_url='')
def create_catagorie(request):
    if request.method == 'POST': # If the form has been submitted...
        form = createcategorieënform(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            form.save() # Save the form data to the database
            return redirect('directie-homepage')  # Redirect to a success page or another view
    else:
        form = createcategorieënform() # An unbound form

    return render(request, 'directie/Categorieëtoevoegen.html', {'form': form})