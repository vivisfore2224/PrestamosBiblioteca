from django.urls import path

from gestionPrestamos.views import LibroView, PrestamoView, DevolucionView
from gestionPrestamos.viewsFrontend import *
from gestionPrestamos.viewLogin import *

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
    path('prueba/',prueba,name='prueba'),
    path('cargarForm/<str:isbn>', cargarForm, name='formulario'),
    path('actualizarLibro/', actualizarLibro, name='actualizar'),
    path('eliminarLibro/<str:isbn>', eliminarLibro, name='eliminar'),
    path('ingresar/', iniciarSesion, name='ingresar'),
    path('cerrar/', cerrarSesion, name='cerrar'),
    path('listaLibrosEst/', listaLibrosEst, name="listaLibrosEst"),
    path('consultaLibroEst/', consultaLibroEst, name="consultaLibroEst")
    
]
