from django.contrib import admin
from consultasubsidio.models import documento, subsidios, departamento, municipio, aplica

# Register your models here.
admin.site.register(documento)
admin.site.register(subsidios)
class deparAdmin(admin.ModelAdmin):
    list_display=("id", "nombre")
    search_fields=["nombre"]
admin.site.register(departamento, deparAdmin)
admin.site.register(municipio)
admin.site.register(aplica)