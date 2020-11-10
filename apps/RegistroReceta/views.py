from django.shortcuts import render, redirect
from .models import Receta
# from .forms import RecetaForm



# Create your views here.

# def crear_receta(request):
#     if request.method == "POST":
#         form = RecetaForm(request.POST)
#         if form.is_valid():
#             model_instance = form.save(commit=False)
#             model_instance.save()
#             return redirect("/crear-receta")
#     else:
#         form = RecetaForm()
#         return render(request, "RegistroReceta/crear-receta.html", {'form': form})


