from django.shortcuts import render
from django.views.generic import CreateView, DetailView
from accounts.forms import UserCreationForm
from accounts.models import User
from django.urls import reverse_lazy

# Create your views here.

class RegisterView(CreateView):
    form_class = UserCreationForm
    model = User
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('blog:home')

class ProfileView(DetailView):
    template_name = 'accounts/profile.html'
    model = User
    slug_field = 'username'
    slug_url_kwarg = 'username'
    context_object_name = "user_object"