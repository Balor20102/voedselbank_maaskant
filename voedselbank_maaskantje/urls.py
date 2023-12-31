"""voedselbank_maaskantje URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from login.views import LoginView, HomeView
from directie.views import *
from klanten.views import *

from magazijn.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", LoginView.as_view(), name="login"),
    path("home/", HomeView.as_view(), name="home"),
    path("logout/", LogoutView.as_view(next_page='login'), name="logout"),
    path('create-catagorie/', create_catagorie, name='create-catagorie'),
    path('catagorie-aanpassen/<int:id>/', catagorie_aanpassen, name='catagorie-aanpassen'),
    path('catagorieën/', catagorieën, name='catagorieën'),
    path('directiehomepage/', directiehomepage, name='directiehomepage'),
    path('verwijder_catagorie/<int:id>/', verwijder_catagorie, name='verwijder_catagorie'),
    path('directie-homepage/', directiehomepage, name='directie-homepage'),
    path('verwijder-catagorie/<int:id>/', verwijder_catagorie, name='verwijder-catagorie'),
    path("voorraad-medewerker/", StockEmployeView.as_view(), name="stock-employe"),
    path("voorraad-medewerker/toevoegen/", AddStockView.as_view(), name="add-stock"),
    path("leveranciers/", leveranciers, name="leveranciers"),
    path("voorraad-medewerker/update/<int:id>", UpdateStockView.as_view(), name="update-stock"),

    path("product/overzicht/<int:id>", ProductItemView.as_view(), name="product-item"),
    path("product/overzicht/<int:id>/toevoegen", AddProductItem.as_view(), name="product-item-add"),
    path("product/overzicht/<int:id>/update/<int:iditem>", UpdateProductItem.as_view(), name="product-item-update"),
    path("product/overzicht/<int:id>/verwijderen/<int:iditem>", DeleteProductItem.as_view(), name="product-item-delete"),
    path("pakket/<int:pk>", PakketView.as_view(), name="pakket"),	
    path("pakket_kiezen/", ChoicePackage.as_view(), name="pakket_kiezen"),
    path("pakket/toevoegen/<int:product>/<int:pakket>/<int:hoeveel>", ToevoegenPakketView.as_view(), name="toevoegen_pakket"),
    path("pakketten/<int:id>", PakketDetailView.as_view(), name="pakketten_detail"),
    path("pakketten/verwijderen/<int:product>/<int:pakket>/<int:hoeveel>", VerwijderenPakketView.as_view(), name="pakketten_verwijderen"),
    path("product/overzicht/<int:id>/update/<int:iditem>", UpdateProductItem.as_view(), name="product-item-update"),	
    path('verwijder-medewerkers/<int:id>/', verwijder_medewerkers, name='verwijder-medewerkers'),
    path('klanten/', klanten, name='klanten'),
    path('klanten/toevoegen/', create_klanten, name='create-klanten'),
    path('klanten-aanpassen/<int:id>/', klanten_aanpassen, name='klanten-aanpassen'),
    path('verwijder-klanten/<int:id>/', verwijder_klanten, name='verwijder-klanten'),
    path('verwijder-leveranciers/<int:id>/', verwijder_leveranciers, name='verwijder-leveranciers'),
    path('leveranciers-aanpassen/<int:id>/', leveranciers_aanpassen, name='leveranciers-aanpassen'),
    path("leveranciers/toevoegen/", create_leveranciers, name="add-leverancier"),
    path('medewerker-registratie/', register, name='medewerker-registratie'),
    path('medewerkers/', Medewerkers, name='medewerkers'),
    
    path('rapportages/', RapportagesView.as_view(), name='rapportages'),
    path('rapportages/ingaand', PCRapportage.as_view(), name='rapportage-ingaand'),
    path('rapportages/uitgaand/', UitgaatRapportage.as_view(), name='rapportages-uitgaand'),
    path('allergieen-toevoegen/', Allergieen.as_view(), name='allergieen'),
    path('allergieen-aanpassen/<int:id>/', allergieen_aanpassen, name='allergieen-aanpassen'),
    path('allergieen/', alergie, name='allergieen-overzicht'),
    path('verwijder_allergieen/<int:id>/', verwijder_allergie, name='verwijder_allergieen'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
