from django.shortcuts import render

from django.contrib.auth.models import User
from .forms import RegistroForm
from django.views.generic import CreateView, UpdateView, DetailView
from django.urls import reverse_lazy

# Create your views here.

class RegistroUsuario(CreateView):
    model = User
    template_name = "RegistroUsuario/registro.html"
    form_class = RegistroForm
    # TODO: descomentar cuando se configure el home
    # success_url = reverse_lazy('home')