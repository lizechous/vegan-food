from django.urls import path, include
from . import views




urlpatterns = [   
        # agregar receta
    path('crearReceta', views.crear_receta, name="crear_receta"),
        # listar las carreras de la bd
    path('listarRecetas', views.listar_recetas, name="listar_recetas"),
    # editar receta
    path('editarReceta/<int:receta_id>', views.editar_receta ,name="editar_receta"),
    # borrar receta
    path('borrarReceta/<int:receta_id>', views.borrar_receta, name="borrar_receta"),
    
    path('index', views.index, name="index"),
    path('registro', views.registro, name="registro"),
    path('contacto', views.contacto, name="contacto"),
    path('ingresar', views.ingresar, name="ingresar"),
]

