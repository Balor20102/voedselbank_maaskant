from django.shortcuts import render

def directiehomepage(request):
    return render(request, 'directie/homepagina.html')