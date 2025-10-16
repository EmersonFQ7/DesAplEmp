# courses/models.py

from django.db import models

class Instructor(models.Model):
    nombre = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Curso(models.Model):
    NIVEL_CHOICES = [
        ('Básico', 'Básico'),
        ('Intermedio', 'Intermedio'),
        ('Avanzado', 'Avanzado'),
    ]

    nombre = models.CharField(max_length=200)
    duracion = models.PositiveIntegerField(help_text="Duración en horas")
    nivel = models.CharField(max_length=20, choices=NIVEL_CHOICES)
    instructor = models.ForeignKey(Instructor, related_name='cursos', on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre