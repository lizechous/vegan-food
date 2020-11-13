from django import forms
from .models import Receta


class RecetaForm(forms.ModelForm):
    class Meta:
        model = Receta
        fields = ['nombre_receta', 'porciones', 'tipo_receta', 'ingredientes', 'instrucciones', 'imagen']
        labels = {
            'nombre_receta': 'Receta',
            'porciones': 'Porciones',
            'tipo_receta': 'Tipo receta',
            'ingredientes': 'Ingredientes',
            'instrucciones': 'Instrucciones',
            'imagen': 'Imagen Receta'
            

        }
        widgets = {
            'nombre_receta': forms.TextInput(attrs={'class': 'form-control'}),
            'porciones': forms.NumberInput(attrs={'class': 'form-control'}),
            'tipo_receta': forms.Select(choices="TIPO_RECETA", attrs={'class':'form-control'}),
            'ingredientes': forms.Textarea(attrs={'class': 'form-control'}),
            'instrucciones': forms.Textarea(attrs={'class': 'form-control'}),
        }
