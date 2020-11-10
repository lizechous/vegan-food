from django import forms
from .models import Receta


# class RecetaForm(forms.ModelForm):
#     class Meta:
#         model = Receta
#         fields = ['nombre_receta', 'porciones', 'tipo_receta', 'ingredientes', 'instrucciones', 'imagen']
#         labels = {
#             'nombre_receta': 'Receta',
#             'porciones': 'Porciones',
#             'tipo_receta': 'Tipo receta',
#             'ingredientes': 'Ingredientes',
#             'instrucciones': 'Instrucciones',
#             'imagen': 'Imagen Receta'
            

#         }
#         widgets = {
#             'nombre_receta': forms.TextInput(attrs={'class': 'form-control'}),
#             'porciones': forms.TextInput(attrs={'class': 'form-control'}),
#             'tipo_receta': forms.TextInput(attrs={'class': 'form-control'}),
#             'ingredientes': forms.TextInput(attrs={'class': 'form-control'}),
#             'instrucciones': forms.TextInput(attrs={'class': 'form-control'}),
#             'imagen': forms.FileInput(attrs={'class': 'form-control'}),
#         }
