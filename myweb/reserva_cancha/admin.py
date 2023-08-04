from django.contrib import admin
from .models import Usuario, Cancha, Reserva, Tipo_Cancha

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('ci_numero', 'nombre', 'email', 'direccion', 'telefono', 'contraseña')
    #list_filter = ('ci_numero', 'nombre')
    #ordering = ['nombre']

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ('id_usuario', 'fecha', 'hora_entrada', 'hora_salida', 'monto', 'id_cancha', 'estado')
    #list_filter = ('ci_numero', 'nombre')
    #ordering = ['nombre']

@admin.register(Cancha)
class CanchaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'id_tipo_cancha', 'direccion', 'costo_hora', 'hora_apertura', 'hora_cierre')
    #list_filter = ('ci_numero', 'nombre')
    #ordering = ['nombre']

@admin.register(Tipo_Cancha)
class Tipo_CanchaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'capacidad')
    #list_filter = ('ci_numero', 'nombre')
    #ordering = ['nombre']
