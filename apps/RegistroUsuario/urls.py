from django.urls import path, include
from .views import RegistroUsuario

urlpatterns = [
    path('registro', RegistroUsuario.as_view(), name="registro"),
]
