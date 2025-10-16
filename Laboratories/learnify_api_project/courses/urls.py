from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import InstructorViewSet, CursoViewSet

# Crea un router y registra nuestros viewsets
router = DefaultRouter()
router.register(r'instructores', InstructorViewSet, basename='instructor')
router.register(r'cursos', CursoViewSet, basename='curso')

# Las URLs de la API son determinadas automáticamente por el router
urlpatterns = [
    path('', include(router.urls)),
]