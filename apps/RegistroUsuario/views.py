from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from .forms import RegistroForm, CuentaForm
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordResetForm
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes


# CRUD

class RegistroUsuario(CreateView):
    model = User
    template_name = "RegistroUsuario/formulario.html"
    form_class = RegistroForm
    success_url = reverse_lazy('login')

class CuentaUsuario(UpdateView):
    model = User
    form_class = CuentaForm
    template_name = "RegistroUsuario/formulario.html"
    # TODO: este redirect no sirve (al menos no así pelao)
    success_url = reverse_lazy('cuenta')

class EliminarUsuario(DeleteView):
    pass


# Metodos personalizados

def listar_recetas_usuario(request, user_id):
    pass


def password_reset_request(request):
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = User.objects.filter(Q(email=data))
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "RegistroUsuario/password_reset_email.txt"
                    c = {
                    "email":user.email,
                    'domain':'127.0.0.1:8000',
                    'site_name': 'Website',
                    "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                    "user": user,
                    'token': default_token_generator.make_token(user),
                    'protocol': 'http',
                    }
                    email = render_to_string(email_template_name, c)
                    try:
                        send_mail(subject, email, 'admin@example.com' , [user.email], fail_silently=False)
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                    return redirect ("/password_reset/done/")
    password_reset_form = PasswordResetForm()
    return render(request=request, template_name="RegistroUsuario/password_reset.html", context={"password_reset_form":password_reset_form})