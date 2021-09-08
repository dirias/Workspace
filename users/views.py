from django.shortcuts import redirect,render
# Django
from django.urls import reverse_lazy
from django.contrib.auth import logout, views as auth_views
from django.contrib.auth.decorators import login_required
from django.views.generic import FormView
from users.forms import SignupForm
# Importing forms


# Create your views here.
class SignupView(FormView):
    """Users sign up class view."""

    template_name = 'users/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('users:login')
    # To save the data
    def form_valid(self, form):
        """Save form data."""
        form.save()
        return super().form_valid(form)

@login_required
def home(request):
    return render(request=request, template_name='users/home.html', context={})

class LoginView(auth_views.LoginView):
    """Login view."""
    template_name = 'users/login.html'
    
@login_required
def logout_view(request):
    """Loging out """
    logout(request)
    return redirect('users:logout')