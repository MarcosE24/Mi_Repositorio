from django.contrib import admin
from .models import Usuario, Cancha, Reserva, Tipo_Cancha, Deporte

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('ci_numero', 'nombre', 'email', 'direccion', 'telefono', 'contraseña')
    list_filter = ('ci_numero', 'nombre', 'direccion')
    ordering = ['nombre']

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ('id_usuario', 'fecha', 'hora_entrada', 'hora_salida', 'monto', 'id_cancha', 'estado')
    list_filter = ('id_usuario', 'fecha', 'id_cancha')
    ordering = ['fecha']

@admin.register(Cancha)
class CanchaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'id_tipo_cancha', 'localidad', 'direccion', 'costo_hora', 'hora_apertura', 'hora_cierre')
    list_filter = ('nombre', 'id_tipo_cancha', 'localidad')
    ordering = ['nombre']

@admin.register(Tipo_Cancha)
class Tipo_CanchaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'capacidad')
    list_filter = ('nombre', 'capacidad')
    ordering = ['nombre']

@admin.register(Deporte)
class DeporteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')
    ordering = ['nombre']