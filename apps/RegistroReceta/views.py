from django.shortcuts import render, redirect, get_object_or_404
from .models import Receta
from .forms import RecetaForm
from django.urls import reverse_lazy

from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.db.models import Q

#------------- importaciones API ---------------------
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import RecetaSerializer
from rest_framework import status

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 

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
    recetas = Receta.objects.all()
    if request.user.is_superuser == False:
        recetas = recetas.filter(autor_id = id_autor)
    # return render(request, "RegistroReceta/listar_recetas.html", {'recetas': recetas})
# -----------------------------
    nombre_receta= request.GET.get('nombre-receta')
    tipo_receta= request.GET.get('tipo-receta')

    if 'btn-buscarReceta' in request.GET:
        if nombre_receta != '':
            recetas = recetas.filter(nombre_receta__icontains=nombre_receta)
        if tipo_receta != 'Todos':
            recetas = recetas.filter(tipo_receta__icontains= tipo_receta)

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

#----------------- API --------------------

@api_view(['GET', 'POST'])
def receta_collection(request):
    if request.method == 'GET':
        recetas = Receta.objects.all()
        serializer = RecetaSerializer(recetas, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = RecetaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def receta_element(request, pk):
    receta = get_object_or_404(Receta, id=pk)

    if request.method == 'GET':
        serializer = RecetaSerializer(receta)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        receta.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PUT': 
        receta_new = JSONParser().parse(request) 
        serializer = RecetaSerializer(receta, data=receta_new) 
        if serializer.is_valid(): 
            serializer.save() 
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

