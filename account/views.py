from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .forms import CustomUserCreationForm, CustomAuthenticationForm


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


class MyLoginView(LoginView):
    form_class = CustomAuthenticationForm
    template_name = "registration/login.html"

@login_required
def account_view(request):
    return render(request, 'registration/account.html', {'user': request.user})