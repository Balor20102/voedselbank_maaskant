from django.views import View

from django.shortcuts import render, redirect

from django.contrib.auth.mixins import LoginRequiredMixin

from directie.forms import createAlergieform


class Allergieen(LoginRequiredMixin, View):
    def get(self, request):
        form = createAlergieform()
        return render(request, 'directie/allergieen.html' , {'form': form})

    def post(self, request):
        form = createAlergieform(request.POST)
        if form.is_valid():
            form.save()
            redirect('directiehomepage')
        return redirect('directiehomepage')
    