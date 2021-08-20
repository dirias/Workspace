from django.shortcuts import HttpResponse
# Django
from django.contrib.auth import views as auth_views
# Importing forms


# Create your views here.
def login(request):
    return HttpResponse('Hola Mundo!')

class LoginView(auth_views.LoginView):
    """Login view."""
    template_name = 'users/login.html'
