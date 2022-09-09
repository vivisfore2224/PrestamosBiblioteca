from django.urls import path

from gestionPrestamos.views import LibroView

urlpatterns = [
    path('Libros/', LibroView.as_view(), name='Listar'),
    path('Libros/<str:isbn>', LibroView.as_view(), name='Buscar')
]
