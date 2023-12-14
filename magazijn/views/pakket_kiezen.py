from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import render
from django.utils import timezone
from datetime import timedelta
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from magazijn.models import Pakket
from klanten.models import Klant


class ChoicePackage(LoginRequiredMixin, View):


    model = Pakket
    klant_model = Klant
    template_name = "magazijn/pakket_kiezen.html"
    items_per_page = 10  # Set the number of items per page

    def get(self, request):
        seven_days_ago = timezone.now() - timedelta(days=7)
        recent_pakket_ids = Pakket.objects.filter(aangemaakt_op__range=(seven_days_ago, timezone.now())).values_list('gezinsnaam_id', flat=True)
        klanten_without_recent_pakket = Klant.objects.exclude(id__in=recent_pakket_ids)

        # Paginate the results
        page_number = request.GET.get('page', 1)
        paginator = Paginator(klanten_without_recent_pakket, self.items_per_page)

        try:
            klanten_page = paginator.page(page_number)
        except PageNotAnInteger:
            klanten_page = paginator.page(1)
        except EmptyPage:
            klanten_page = paginator.page(paginator.num_pages)

        context = {
            'klanten_page': klanten_page,
        }
        return render(request, self.template_name, context)