from django.db import models

class Profesor(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    contraseña = models.CharField(max_length=255)  # Encriptada
    direccion = models.TextField()
    departamento = models.CharField(max_length=100)
    identificacion = models.CharField(max_length=50)
    codigo_profesor = models.CharField(max_length=50)
    telefono = models.CharField(max_length=15)
    codigo_clase = models.CharField(max_length=50)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre
