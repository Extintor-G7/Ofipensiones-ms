import os
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
            reporte.obtener_facturas(id_colegio,ENCRYPTION_KEY)  # This will generate the CSV and encrypt it

            # Path to the encrypted file
            archivo_encriptado = f'reportes/reportesCsv/reporte_{id_colegio}.csv.enc'

            # Decrypt the file and send it back to the user
            with open(archivo_encriptado, 'rb') as file:
                encrypted_data = file.read()
                cipher_suite = Fernet(ENCRYPTION_KEY)
                decrypted_data = cipher_suite.decrypt(encrypted_data)

            # Return the decrypted file as a response for download
            response = HttpResponse(decrypted_data, content_type='text/csv')
            response['Content-Disposition'] = f'attachment; filename="reporte_{id_colegio}.csv"'
            return response

        except Reporte.DoesNotExist:
            return HttpResponse(f"No se encontró el colegio con ID: {id_colegio}")

    return render(request, 'generar_csv.html')
