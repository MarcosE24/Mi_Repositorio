from django.db import models
class Usuario (models.Model):
    ci_numero=models.IntegerField(blank=False, default=0)
    nombre=models.CharField(max_length=150, blank=False)
    email=models.CharField(max_length=100, blank=False)
    direccion=models.CharField(max_length=100, blank=False)
    telefono=models.IntegerField(blank=False, default=0)
    contraseña=models.CharField(max_length=100, blank=False)
    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name_plural="Usuarios"

class Tipo_Cancha(models.Model):
    nombre=models.CharField(max_length=150, blank=False)
    capacidad=models.IntegerField(blank=False, default=0)
    class Meta:
        verbose_name_plural = "Tipos de Cancha"

class Cancha(models.Model):
    nombre=models.CharField(max_length=150, blank=False)
    id_tipo_cancha=models.ForeignKey(Tipo_Cancha, on_delete=models.CASCADE)
    direccion=models.CharField(max_length=150, blank=False)
    costo_hora=models.IntegerField()
    hora_apertura=models.TimeField()
    hora_cierre=models.TimeField()
    class Meta:
        verbose_name_plural = "Canchas"

class Reserva(models.Model):
    id_usuario=models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha=models.DateField()
    hora_entrada=models.TimeField()
    hora_salida=models.TimeField()
    monto=models.IntegerField()
    id_cancha=models.ForeignKey(Cancha, on_delete=models.CASCADE)
    estado=models.CharField(max_length=50)
    class Meta:
        verbose_name_plural = "Reservas"