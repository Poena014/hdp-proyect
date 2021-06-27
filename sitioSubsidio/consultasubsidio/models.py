from django.contrib.auth.models import User
from django.db import models

# Create your models here.
# auth system
# documento
# departamento
# Municipio
# Direccion
# Subsidios
#Subsidios Aplica
#

class departamento(models.Model):
    nombre=models.CharField(max_length=30)
    class Meta:
        ordering=["nombre"]

class municipio(models.Model):
    nombre=models.CharField(max_length=30)


class documento(models.Model):
    usuario=models.ForeignKey(User, on_delete=models.CASCADE)
    dui=models.CharField( max_length=12, unique=True, verbose_name="dui")
    depar=models.ForeignKey(departamento, on_delete=models.CASCADE)
    muni=models.ForeignKey(municipio, on_delete=models.CASCADE)
    dire=models.CharField(max_length=200, default="Sin Informacion")
    telefono=models.CharField( max_length=8, default="00000000")

    class Meta:
        ordering=["dui"]

class subsidios(models.Model):
    nombre=models.CharField(max_length=50)
    fecha=models.DateField()
    monto=models.FloatField( default=0.0)
    descripcion=models.CharField(max_length=300, default="Sin informacion")
    duracion=models.IntegerField(default=0)
    estado=models.BooleanField(default=False)



class aplica(models.Model):
    persona=models.ForeignKey(documento, on_delete=models.CASCADE)
    subsidio=models.ForeignKey(subsidios, on_delete=models.CASCADE)
    estado=models.BooleanField(default=False);


