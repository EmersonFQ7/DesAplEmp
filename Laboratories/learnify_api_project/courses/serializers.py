from rest_framework import serializers
from .models import Instructor, Curso

class InstructorSerializer(serializers.ModelSerializer):
    # Para mostrar los nombres de los cursos en lugar de solo sus IDs
    cursos = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Instructor
        fields = ['id', 'nombre', 'especialidad', 'cursos']

class CursoSerializer(serializers.ModelSerializer):
    # Para mostrar el nombre del instructor en las respuestas GET
    instructor_nombre = serializers.CharField(source='instructor.nombre', read_only=True)
    
    class Meta:
        model = Curso
        # 'instructor' se usará para escribir (recibe un ID), 
        # 'instructor_nombre' se usará para leer (devuelve un string)
        fields = ['id', 'nombre', 'duracion', 'nivel', 'instructor', 'instructor_nombre']