from django.urls import URLPattern, path
from .import views

urlpatterns = [
    path('cargarAlumnos/', views.cargar_alumno, name='cargar_alumnos'), # type: ignore
    path('listarAlumnos/', views.listar_alumno, name='listarAlumnos'), # type: ignore
    # Resta crear los paths para modificar, eliminar, asignar y listar por curso
]