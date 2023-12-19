# views.py
from django.contrib.auth import login
from django.shortcuts import render, redirect
from directie.forms import CustomUserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required



@login_required(login_url='')
def Medewerkers(request):
    user_group_array = [] # array met alle users en hun groepen
    for user in User.objects.all(): # loop door alle users
        if user.is_superuser: # als user superuser is, ga verder    
            continue # ga verder
        group_names = [group.name for group in user.groups.all()] # haal alle groepen op van user
        user_group_array.append({"user": user, "groups": group_names, "id": user.id}) # voeg user en groepen toe aan array


    context = {'werknemer': user_group_array} # maak context aan
    return render(request, 'directie/medewerkers.html', context) # render pagina met context


@login_required(login_url='') # check of user ingelogd is
def register(request): # functie voor registreren van medewerkers
    if request.method == 'POST': # check of request een POST request is
        form = CustomUserCreationForm(request.POST) # maak form aan met POST data
        if form.is_valid(): # check of form valid is
            user = form.save() # sla form op
            group = form.cleaned_data['group']  # haal groep op uit form
            user.groups.add(group) # voeg groep toe aan user
            return redirect('directie-homepage')  # Replace 'home' with your desired redirect URL
        redirect('medewerker-registratie') # redirect naar registratie pagina
    else:
        form = CustomUserCreationForm() # maak form aan
    return render(request, 'directie/medewerkers_registreren.html', {'form': form})


@login_required(login_url='')
def verwijder_medewerkers(request, id):
    user = User.objects.get(id=id)
    user.delete()
    return redirect('medewerkers')
