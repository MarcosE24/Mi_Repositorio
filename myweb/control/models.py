from django.db import models

class Empleado (models.Model):
    turnos=(("opcion1","Mañana"),
              ("opcion2","Tarde"),
              ("opcion3","Noche"),
    )
    nombre=models.CharField(max_length=150, blank=False)
    departamento=models.CharField(max_length=100, blank=False)
    fecha_inicio=models.DateField(auto_now_add=True, blank=False)
    dias_trabajo=models.CharField(max_length=100, blank=False)
    turno=models.CharField(blank=False, choices=turnos, max_length=50)
    hora_entrada=models.TimeField(blank=False)
    hora_salida=models.TimeField(blank=False)
    activo=models.BooleanField(blank=True,default=True)
    telefono=models.IntegerField(blank=True, default=0)
    def __str__(self):
        return self.nombre

class Jornada (models.Model):
    marcacion=(("opcion1","Entrada"),
              ("opcion2","Salida"),
    )
    id_empleado=models.ForeignKey(Empleado, on_delete=models.CASCADE)
    fecha=models.DateTimeField(blank=False)
    tipo_marcacion=models.CharField(blank=False, choices=marcacion, max_length=50)
    def __str__(self):
        return self.id_empleado.nombre