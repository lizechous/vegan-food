# Generated by Django 3.1.2 on 2020-11-12 21:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('RegistroReceta', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receta',
            name='autor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='receta',
            name='tipo_receta',
            field=models.CharField(choices=[('Pasteles', 'Pasteles'), ('Postres', 'Postres'), ('Comidas', 'Comidas'), ('Bebestibles', 'Bebestibles')], max_length=50),
        ),
    ]