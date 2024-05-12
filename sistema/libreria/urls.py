from django.urls import path
from . import views # Importamos las vistas de la libreria

urlpatterns = [
    path('', views.inicio, name='inicio'), # Ruta de la pagina de inicio
    path('nosotros', views.nosotros, name='nosotros'), # Ruta de la pagina nosotros
    path('libros', views.libros, name='libros'), # Ruta de la pagina libros
]