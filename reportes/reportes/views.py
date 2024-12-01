import os
import time
from django.http import HttpResponse
from django.shortcuts import render
from .models import Reporte
from cryptography.fernet import Fernet

# Generate the encryption key once (this could be stored securely in production)
ENCRYPTION_KEY = Fernet.generate_key()

def generar_csv_view(request):
    if request.method == 'POST':
        id_colegio = request.POST.get('idColegio')

        try:
            # Fetch the report for the given id_colegio (it might be a different ID)
            reporte = Reporte.objects.get(id=1)

            # Fetch the invoices based on the colegio id and pass the encryption key
            timestamp = int(time.time())
            reporte.obtener_facturas(id_colegio,ENCRYPTION_KEY,timestamp)  # This will generate the CSV and encrypt it

            # Path to the encrypted file
            archivo_encriptado = f'reportes/reportesCsv/reporte_{timestamp}.csv.enc'

            # Decrypt the file and send it back to the user
            with open(archivo_encriptado, 'rb') as file:
                encrypted_data = file.read()
                cipher_suite = Fernet(ENCRYPTION_KEY)
                decrypted_data = cipher_suite.decrypt(encrypted_data)

            # Return the decrypted file as a response for download
            response = HttpResponse(decrypted_data, content_type='text/csv')
            response['Content-Disposition'] = f'attachment; filename="reporte_{timestamp}.csv"'
            return response

        except Reporte.DoesNotExist:
            return HttpResponse(f"No se encontró el colegio con ID: {id_colegio}")

    return render(request, 'generar_csv.html')

def descargar_csv_no_encriptado_view(request):
    if request.method == 'POST':
        id_colegio = request.POST.get('idColegio')

        try:
            # Fetch the report for the given id_colegio (it might be a different ID)
            reporte = Reporte.objects.get(id=1)
            timestamp = int(time.time())
            # Fetch the invoices based on the colegio id and generate the CSV without encryption
            facturas = reporte.obtener_facturas2(id_colegio,timestamp)  # Assuming it generates the non-encrypted CSV
            
            # Path to the non-encrypted CSV file
            archivo_csv = f'reportes/reportesCsv/reporte_{timestamp}.csv'

            # Check if the file exists
            if not os.path.exists(archivo_csv):
                return HttpResponse(f"El archivo CSV para el colegio con ID {id_colegio} no fue encontrado.", status=404)

            # Return the non-encrypted file as a response for download
            with open(archivo_csv, 'rb') as file:
                file_data = file.read()

            response = HttpResponse(file_data, content_type='text/csv')
            response['Content-Disposition'] = f'attachment; filename="reporte_{timestamp}.csv"'
            return response

        except Reporte.DoesNotExist:
            return HttpResponse(f"No se encontró el colegio con ID: {id_colegio}")

    return render(request, 'generar_csv2.html')
