from django.views import View

from django.shortcuts import render, redirect

from django.contrib.auth.mixins import LoginRequiredMixin

from directie.forms import createAlergieform


class Allergieen(LoginRequiredMixin, View):
    def get(self, request):
        form = createAlergieform() # maak form aan
        return render(request, 'directie/allergieen.html' , {'form': form})

    def post(self, request):
        form = createAlergieform(request.POST) # maak form aan met POST data
        if form.is_valid(): # check of form valid is
            form.save() # sla form op
            redirect('directiehomepage')
        return redirect('directiehomepage')
    