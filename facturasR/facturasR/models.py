from django.db import models

# Create your models here.
class Factura(models.Model):
    id = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=100)
    precio = models.IntegerField()
    fechaPago = models.DateField()
    idColegio = models.IntegerField()
    
