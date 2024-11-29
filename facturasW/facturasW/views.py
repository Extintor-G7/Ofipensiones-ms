from .models import Factura
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
import requests
import json

# Create your views here.
def FacturaCreate(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        data_json = json.loads(data)
        
        factura = Factura()
        factura.tipo = data_json['tipo']
        factura.precio = data_json['precio']
        factura.fechaPago = data_json['fechaPago']
        factura.idColegio = data_json['idColegio']
        factura.save()
        return HttpResponse("successfully created measurement")
        