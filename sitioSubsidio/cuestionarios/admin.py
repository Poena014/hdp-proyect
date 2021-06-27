from django.contrib import admin


from cuestionarios.models import cuestionario, pregunta, item_pregunta, registrado, registro

# Register your models here.

class cuestionarioAdmin(admin.ModelAdmin):
    list_display=("id", "nombre", "estado", "fecha")
    search_fields=["nombre", "estado", "fecha", "id"]

admin.site.register(cuestionario, cuestionarioAdmin)

class preguntaAdmin(admin.ModelAdmin):
    list_display=( "id","texto_pregunta", "tipopreguntas")
    search_fields=["texto_pregunta"]

admin.site.register(pregunta, preguntaAdmin)


class itemAdmin(admin.ModelAdmin):
    list_display=("id", "contenido")

admin.site.register(item_pregunta, itemAdmin)

admin.site.register(registrado)
admin.site.register(registro)