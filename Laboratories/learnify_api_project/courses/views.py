from rest_framework import viewsets, filters
from .models import Instructor, Curso
from .serializers import InstructorSerializer, CursoSerializer

class InstructorViewSet(viewsets.ModelViewSet):
    """
    API endpoint que permite ver, crear, editar y eliminar Instructores.
    """
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer

class CursoViewSet(viewsets.ModelViewSet):
    """
    API endpoint para Cursos.
    Permite búsqueda por nombre y nivel a través del parámetro 'search'.
    Ej: /api/cursos/?search=Python
    """
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['nombre', 'nivel']