from django.views import View

from django.shortcuts import render, redirect

class RapportagesView(View):
    """RapportagesView klasse.

    View voor het renderen van de rapportages pagina.
    """
    template_name = 'directie/rapportages.html'

    def get(self, request):
        """GET request voor het renderen van de pagina.

        :param request: het http request
        :type request: HttpRequest
        :return: gerenderde pagina
        :rtype: HttpResponse
        """
        return render(request, self.template_name)