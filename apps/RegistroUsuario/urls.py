from django.urls import path, include
from django.contrib.auth.views import login_required
from .views import RegistroUsuario, CuentaUsuario

urlpatterns = [
    path("registro/", RegistroUsuario.as_view(), name="registro"),
    path("cuenta/<int:pk>", login_required(CuentaUsuario.as_view()), name="cuenta"),
]
