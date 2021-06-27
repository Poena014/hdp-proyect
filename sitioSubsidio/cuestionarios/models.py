from django.db import models
import datetime

# Create your models here.
class cuestionario(models.Model):
    nombre=models.CharField(max_length=50, default="Cuestionario")
    estado=models.BooleanField(null=False, default=True)
    fecha=models.DateField(null=True);
    descripcion=models.CharField(max_length=200, null=True, blank=True)
    alcance=models.BooleanField()


    class Meta:
        ordering=["nombre"]


class pregunta(models.Model):
    cuestionario=models.ForeignKey(cuestionario, on_delete=models.CASCADE, related_name='cuestio')
    tipos = [
        ('CH', 'checkbox'),
        ('TX', 'text'),
        ('NUM', 'number'),
    ]
    tipopreguntas=models.CharField(max_length=20,choices=tipos)
    texto_pregunta=models.CharField(max_length=300)

    
    class Meta:
        ordering=["texto_pregunta"]


class item_pregunta(models.Model):
    preguntas=models.ForeignKey(pregunta, on_delete=models.CASCADE)
    
    contenido=models.CharField(max_length=200)


    class Meta:
        ordering=["contenido"]
    


class registro(models.Model):
    id=models.AutoField(primary_key=True)
    fecha=models.DateField(null=True)


    class Meta:
        ordering=["fecha"]

class registrado(models.Model):
    registros=models.ForeignKey(registro, on_delete=models.CASCADE)
    cuestionarios=models.ForeignKey(cuestionario, on_delete=models.CASCADE)
    preguntas=models.ForeignKey(pregunta, on_delete=models.CASCADE)
    item_preguntas=models.ForeignKey(item_pregunta, on_delete=models.CASCADE)
    guardado=models.CharField(max_length=200, null=False, blank=False, default="Sin informacion")
    class Meta:
        ordering=["registros"]



    

