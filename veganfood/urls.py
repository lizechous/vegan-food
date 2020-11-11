"""veganfood URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', include('apps.RegistroReceta.urls')),

    path('usuario/',include('apps.RegistroUsuario.urls')),
    #TODO: añadir `redirect_authenticated_user=True` cuando esté creado el home
    path('accounts/login/', LoginView.as_view(template_name='RegistroUsuario/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='RegistroUsuario/logout.html'), name='logout'),
    
    path('admin/', admin.site.urls),
]
