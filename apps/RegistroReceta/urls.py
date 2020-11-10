from django.urls import path, include
from . import views

urlpatterns = [
    
    path('crear-receta', views.crear_receta, name="crear-receta"),
    

]

