from django.urls import path

from gestionPrestamos.views import LibroView, PrestamoView, DevolucionView
from gestionPrestamos.viewsFrontend import *

urlpatterns = [
    path('Libros/', LibroView.as_view(), name='Listar'),
    path('Libros/<str:isbn>', LibroView.as_view(), name='Buscar'),
    path('Prestamos/', PrestamoView.as_view(), name='prestamo'),
    path('Devolucion/', DevolucionView.as_view(), name='dev'),
    path('', principal, name="index"),
    path('listaLibros/',listaLibros, name='Lista'),
    path('consultaLibro/', consultaLibro, name='consultarIsbn'),
    path('formLibro/',formularioLibro, name="formulario"),
    path('guardarLibro/', guardarLibro, name='registrar'),
    path('prueba/',prueba,name='prueba')
]
