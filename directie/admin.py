from django.contrib import admin

# Register your models here.

from .models import Leverancier

class LeverancierAdmin(admin.ModelAdmin):
    list_display = ('bedrijfsnaam', 'adres', 'leveringsdatum', 'contactpersoon', 'telefoon', 'email')
    list_filter = ('bedrijfsnaam',)
    search_fields = ('bedrijfsnaam',)
    ordering = ['bedrijfsnaam']

admin.site.register(Leverancier, LeverancierAdmin)