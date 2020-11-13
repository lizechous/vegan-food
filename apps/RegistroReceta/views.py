from django.shortcuts import render, redirect
from .models import Receta
from .forms import RecetaForm
from django.urls import reverse_lazy

from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.db.models import Q

# -------------------------------------
def index(request):
    recetas = Receta.objects.all()
    # return render(request, "RegistroReceta/listar_recetas.html", {'recetas': recetas})
# -----------------------------

    nombre_receta= request.GET.get('nombre-receta')
    tipo_receta= request.GET.get('tipo-receta')

    if 'btn-buscarReceta' in request.GET:
        if nombre_receta != '':
            recetas = Receta.objects.filter(nombre_receta__icontains=nombre_receta)
        if tipo_receta != 'Todos':
            recetas = Receta.objects.filter(tipo_receta__icontains= tipo_receta)
            
    

    return render(request, "index.html", {'recetas': recetas, 'nombreReceta': nombre_receta, 'tipoReceta': tipo_receta})

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
            form.instance.autor_id = request.user.id
            form.save()

            # model_instance.save()
            return redirect("/crearReceta")
    else:
        form = RecetaForm()
    
    
    return render(request, "RegistroReceta/crear_receta.html", {'form': form})

# LISTAR RECETAS
def listar_recetas(request):
    id_autor= request.user.id
    recetas = Receta.objects.filter(autor_id = id_autor)
    # return render(request, "RegistroReceta/listar_recetas.html", {'recetas': recetas})
# -----------------------------
    nombre_receta= request.GET.get('nombre-receta')
    tipo_receta= request.GET.get('tipo-receta')

    if 'btn-buscarReceta' in request.GET:
        if nombre_receta != '':
            recetas = Receta.objects.filter(nombre_receta__icontains=nombre_receta)
        if tipo_receta != 'Todos':
            recetas = Receta.objects.filter(tipo_receta__icontains= tipo_receta)

    return render(request, "RegistroReceta/listar_recetas.html", {'recetas': recetas, 'nombreReceta': nombre_receta, 'tipoReceta': tipo_receta})


# --------------------------------
# VER RECETA
def ver_receta(request, receta_id):
    recetita = Receta.objects.get(id=receta_id)  
    return render(request, "RegistroReceta/ver_receta.html", {'recetita': recetita})
# ------------------------


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

