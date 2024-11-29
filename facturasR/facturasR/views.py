from django.shortcuts import render
from .models import Factura
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.urls import reverse
from django.http import JsonResponse
import json

# Create your views here

def FacturaList(request):
    # Obtener el idColegio del request (usando parámetros de consulta)
    idColegio = request.GET.get('idColegio', None)

    if idColegio is not None:
        # Filtrar facturas por el idColegio proporcionado
        queryset = Factura.objects.filter(idColegio=idColegio)
    else:
        # Si no se proporciona idColegio, devolver todas las facturas
        queryset = Factura.objects.all()

    # Convertir el queryset a una lista de diccionarios
    context = list(queryset.values('id', 'tipo', 'precio', 'fechaPago', 'idColegio'))

    # Retornar la lista como una respuesta JSON
    return JsonResponse(context, safe=False)

