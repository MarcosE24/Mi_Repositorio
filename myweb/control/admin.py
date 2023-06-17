from django.contrib import admin
from . import models

class Empleado (admin.ModelAdmin):
    ordering=["turno"]
    list_display=[field.name for field in models.Empleado._meta.get_fields()]
    list_filter=["nombre"]

class Jornada (admin.ModelAdmin):
    ordering=["fecha"]
    list_display=[field.name for field in models.Jornada._meta.get_fields()]

admin.site.register(models.Empleado)
admin.site.register(models.Jornada)