from django.contrib.auth.views import LoginView as DjangoLoginView

from django.urls import reverse_lazy
from login.forms import LoginForm

class LoginView(DjangoLoginView):
    
    template_name = 'login/login.html'
    success_url = reverse_lazy('home')
