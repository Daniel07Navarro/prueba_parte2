from django.shortcuts import render
from django.contrib import messages
from miapp.models import Pais

# Create your views here.
def index(request):
    return render(request, 'index.html')

def paises(request):
    paises = Pais.objects.all()
    return render(request, 'paises.html', {'paises': paises})

def crear_pais(request):
    return render(request, 'crear_pais.html')

def guardar_pais(request):
    if request.method == 'GET':
        code = request.GET['code']
        nombre = request.GET['nombre']
        poblacion = request.GET['poblacion']
        estado = request.GET['estado']

    pais = Pais(
        code = code,
        nombre = nombre,
        poblacion = poblacion,
        estado = estado
    )
    pais.save()
    paises = Pais.objects.all()
    messages.success(request, f'Se agregó correctamente el artículo {pais.nombre}')
    return render(request, 'paises.html', {'paises': paises})

def eliminar_pais(request,idpais):
    pais=Pais.objects.get(idpais=idpais)
    pais.delete()
    paises = Pais.objects.all()
    return render(request, 'paises.html', {'paises': paises})

def editoriales(request):
    return render(request, 'editoriales.html')

def crear_editorial(request):
    return render(request, 'crear_editorial.html')