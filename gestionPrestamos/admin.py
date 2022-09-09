from django.contrib import admin

# Register your models here.
from gestionPrestamos.models import Libro
from gestionPrestamos.models import Estudiante
from gestionPrestamos.models import Prestamo

admin.site.register(Libro)
admin.site.register(Estudiante)
admin.site.register(Prestamo)