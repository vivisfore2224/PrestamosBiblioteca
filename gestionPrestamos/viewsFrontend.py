from urllib import response
from django.shortcuts import render
from django.http import HttpResponse
import requests

def principal(request):
    return render(request, "index.html")

def listaLibros(request):
    response=requests.get('http://localhost:8000/prestamos/Libros')
    libros=response.json()
    print(libros)
    return render(request, "Libros.html",libros)