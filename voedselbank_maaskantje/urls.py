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
from login.views import LoginView, home
from directie.views import *
from klanten.views import *

from magazijn.views import StockEmployeView, AddStockView
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", LoginView.as_view(), name="login"),
    path("home/", home, name="home"),
    path("logout/", LogoutView.as_view(next_page='login'), name="logout"),
    path('create-catagorie/', create_catagorie, name='create-catagorie'),
    path('catagorie-aanpassen/<int:id>/', catagorie_aanpassen, name='catagorie-aanpassen'),
    path('catagorieën/', catagorieën, name='catagorieën'),
    path('directie-homepage/', directiehomepage, name='directie-homepage'),
    path('verwijder-catagorie/<int:id>/', verwijder_catagorie, name='verwijder-catagorie'),
    path("voorraad-medewerker/", StockEmployeView.as_view(), name="stock-employe"),
    path("voorraad-medewerker/toevoegen/", AddStockView.as_view(), name="add-stock"),
    path("leveranciers/", leveranciers, name="leveranciers"),
    path("leveranciers/toevoegen/", create_leveranciers, name="add-leverancier"),
    path('verwijder-leveranciers/<int:id>/', verwijder_leveranciers, name='verwijder-leveranciers'),
    path('leveranciers-aanpassen/<int:id>/', leveranciers_aanpassen, name='leveranciers-aanpassen'),
    path('klanten/', klanten, name='klanten'),
    path('klanten/toevoegen/', create_klanten, name='create-klanten'),
    path('klanten-aanpassen/<int:id>/', klanten_aanpassen, name='klanten-aanpassen'),
    path('verwijder-klanten/<int:id>/', verwijder_klanten, name='verwijder-klanten'),
    path('medewerker-registratie/', register, name='medewerker-registratie'),
    path('medewerkers/', Medewerkers, name='medewerkers'),
    path('verwijder-medewerkers/<int:id>/', verwijder_medewerkers, name='verwijder-medewerkers'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
