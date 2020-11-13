from django.db import models


# Create your models here.

TIPO_RECETA = (
    ('Pasteles', 'Pasteles'),
    ('Postres', 'Postres'),
    ('Comidas', 'Comidas'),
    ('Bebestibles', 'Bebestibles'),
)


class Receta(models.Model):
    autor = models.ForeignKey('auth.User', default=1, on_delete=models.CASCADE)
    nombre_receta = models.TextField()
    porciones = models.IntegerField()
    tipo_receta = models.CharField(max_length=50, choices=TIPO_RECETA)
    ingredientes = models.TextField()
    instrucciones = models.TextField()
    fecha_creacion =  models.DateTimeField(auto_now_add=True, auto_now=False)
    imagen = models.ImageField(upload_to='RegistroReceta/img/')

    def __str__(self):
        return self.nombre_receta
    
