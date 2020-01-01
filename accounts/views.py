from .forms import CustomUserCreationForm, UserChangeForm
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404 
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


# Create your views here.

class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'