from django.contrib.auth.forms import AuthenticationForm   

def login_navbar(request):
    return {
        'login_navbar_form': AuthenticationForm(),
    }
