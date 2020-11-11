from django.shortcuts import render, redirect
from .models import Receta
from .forms import RecetaForm
from django.urls import reverse_lazy

from django.views.generic import ListView, CreateView, UpdateView, DeleteView

# -------------------------------------
def index(request):
    return render(request, 'index.html')

def registro(request):
    return render(request, 'registro.html')

def contacto(request):
    return render(request, 'contacto.html')

def ingresar(request):
    return render(request, 'ingresar.html')

# ------------------------------------

# Create your views here.

# CREAR RECETA
def crear_receta(request):
    if request.method == "POST":
        form = RecetaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # model_instance.save()
            return redirect("/crearReceta")
    else:
        form = RecetaForm()
    
    
    return render(request, "RegistroReceta/crear_receta.html", {'form': form})

# LISTAR RECETAS
def listar_recetas(request):
    recetas = Receta.objects.all()
    return render(request, "RegistroReceta/listar_recetas.html", {'recetas': recetas})

# EDITAR RECETAS
def editar_receta(request, receta_id):
    instancia = Receta.objects.get(id=receta_id)
    form = RecetaForm(instance=instancia)
    if request.method == "POST":
        form = RecetaForm(request.POST, instance=instancia)
        if form.is_valid():
            instancia = form.save(commit=False)
            instancia.save()
            return redirect('listar_recetas')
    else:
        return render(request, "RegistroReceta/editar_receta.html", {'form': form})

# BORRAR RECETAS
def borrar_receta(request, receta_id):
    instancia = Receta.objects.get(id=receta_id)
    instancia.delete()

    return redirect('listar_recetas')




