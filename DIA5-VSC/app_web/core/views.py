from django.shortcuts import render
from .models import Productos

def index(request):
    productos = Productos.objects.all() #Select * from productos
    context = {
        "misproductos":productos

    }
    template_name="index.html"
    return render(request,template_name,context)


def detalles(request):
    template_name="detalles.html"
    return render(request,template_name)

def acerca(request):
    template_name="acerca.html"
    return render(request,template_name)