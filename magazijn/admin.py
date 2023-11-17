from django.contrib import admin

# Register your models here.

from .models import Product, ProductItem, Catagorie, Pakket

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'EAN', 'varkesvlees', 'vegataries', 'veganistisch')
    list_filter = ('varkesvlees', 'vegataries', 'veganistisch')
    search_fields = ('name', 'EAN')
    ordering = ['name']


class ProductItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'leverings_datum', 'status')
    list_filter = ('status',)
    search_fields = ('product', )
    ordering = ['product']


class CatagorieAdmin(admin.ModelAdmin):
    list_display = ('name', 'omschrijving')
    list_filter = ('name',)
    search_fields = ('name',)
    ordering = ['name']

class PakketAdmin(admin.ModelAdmin):
    list_display = ('gezinsnaam', 'uitgiftdatum')
    list_filter = ('gezinsnaam',)
    search_fields = ('gezinsnaam',)
    ordering = ['gezinsnaam']

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductItem, ProductItemAdmin)
admin.site.register(Catagorie, CatagorieAdmin)
admin.site.register(Pakket, PakketAdmin)
