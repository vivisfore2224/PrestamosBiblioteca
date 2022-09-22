import json
from urllib import response
from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests

def principal(request):
    return render(request, "index.html")

def listaLibros(request):
    response=requests.get('http://localhost:8000/prestamos/Libros')
    libros=response.json()
    print(libros)
    return render(request, "Libros.html",libros)

def consultaLibro(request):
    dato=request.POST['isbn']
    response=requests.get('http://localhost:8000/prestamos/Libros/'+dato)
    libro=response.json()
    print(libro)
    return render(request, 'Libros.html',libro)

def formularioLibro(request):
    return render(request, 'formLibro.html')

def guardarLibro(request):
    datos={
      "Isbn": request.POST['isbn'],
      "titulo": request.POST['titulo'],
      "editorial": request.POST['editorial'],
      "autor": request.POST['autor'],
      "no_page": request.POST['pages']
    }
    requests.post('http://localhost:8000/prestamos/Libros/',data=json.dumps(datos))
    return redirect('../listaLibros/')

def prueba(request):
    response=requests.get('http://localhost:8000/prestamos/Libros')
    libros=response.json()
    print(libros)
    return render(request, "prueba.html",libros)
