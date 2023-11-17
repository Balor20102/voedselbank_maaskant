from django.contrib import admin

# Register your models here.

from .models import Klant, BSN, Alergie

admin.site.register(Klant)
admin.site.register(BSN)
admin.site.register(Alergie)
