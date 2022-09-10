from django.urls import path

from gestionPrestamos.views import LibroView, PrestamoView, DevolucionView

urlpatterns = [
    path('Libros/', LibroView.as_view(), name='Listar'),
    path('Libros/<str:isbn>', LibroView.as_view(), name='Buscar'),
    path('Prestamos/', PrestamoView.as_view(), name='prestamo'),
    path('Devolucion/', DevolucionView.as_view(), name='dev'),
]
