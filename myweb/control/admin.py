from django.contrib import admin
from . import models

class Empleado (admin.ModelAdmin):
    ordering=["-turno"]
    list_display = ('nombre', 'departamento', 'fecha_inicio', 'turno', 'dias_trabajo', 'hora_entrada', 'hora_salida')
    #filtrado por nombre
    list_filter=["nombre"]

class Jornada (admin.ModelAdmin):
    ordering=["-fecha"]
    list_display=[field.name for field in models.Jornada._meta.get_fields()]

admin.site.register(models.Empleado, Empleado)
admin.site.register(models.Jornada, Jornada)