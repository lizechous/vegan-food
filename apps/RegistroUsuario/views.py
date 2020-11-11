from django.shortcuts import render

from django.contrib.auth.models import User
from .forms import UsuarioForm
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


# CRUD

class RegistroUsuario(CreateView):
    model = User
    template_name = "RegistroUsuario/formulario.html"
    form_class = UsuarioForm
    # TODO: redirigir a `home` cuando se configure
    success_url = reverse_lazy('registro')

class CuentaUsuario(UpdateView):
    model = User
    form_class = UsuarioForm
    template_name = "RegistroUsuario/formulario.html"
    success_url = reverse_lazy('cuenta')

class EliminarUsuario(DeleteView):
    pass


# Metodos personalizados

def listar_recetas_usuario(request, user_id):
    pass