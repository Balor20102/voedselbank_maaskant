from django.contrib import admin
from django.contrib.auth.models import Group

# Register your models here.

from .models import Klant, Alergie

admin.site.register(Klant)
admin.site.register(Alergie)
admin.site.unregister(Group)
