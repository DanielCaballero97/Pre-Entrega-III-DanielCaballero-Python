from django.db import models

class Curso(models.Model):
    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()

    def __str__(self):
        return f" Nombre : {self.nombre} | Camada : {self.camada}"

class Estudiante(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=20)
    email = models.EmailField(max_length=40)

    def __str__(self):
        return f" Nombre : {self.nombre} | Apellido : {self.apellido} | Email : {self.email}"

class Profesor(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=20)
    email = models.EmailField(max_length=40)

    def __str__(self):
        return f" Nombre : {self.nombre} | Apellido : {self.apellido} | Email : {self.email}"

class Entregable(models.Model):
    nombre = models.CharField(max_length=30)
    fecha_de_entrega = models.DateField()
    entregado = models.BooleanField()

    def __str__(self):
        return f" Nombre : {self.nombre} | Fecha de entrega : {self.fecha_de_entrega} | Entregado : {self.entregado}"
