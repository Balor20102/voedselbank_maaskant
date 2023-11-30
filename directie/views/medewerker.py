# views.py
from django.contrib.auth import login
from django.shortcuts import render, redirect
from directie.forms import CustomUserCreationForm
from django.contrib.auth.models import User



def Medewerkers(request):
    user_group_array = []
    for user in User.objects.all():
        if user.is_superuser:
            continue
        group_names = [group.name for group in user.groups.all()]
        user_group_array.append({"user": user, "groups": group_names, "id": user.id})


    context = {'werknemer': user_group_array}
    return render(request, 'directie/medewerkers.html', context)

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = form.cleaned_data['group']
            user.groups.add(group)
            return redirect('directie-homepage')  # Replace 'home' with your desired redirect URL
        redirect('medewerker-registratie')
    else:
        form = CustomUserCreationForm()
    return render(request, 'directie/medewerkers_registreren.html', {'form': form})

def verwijder_medewerkers(request, id):
    user = User.objects.get(id=id)
    user.delete()
    return redirect('medewerkers')
