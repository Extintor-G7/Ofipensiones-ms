import csv
import os
from cryptography.fernet import Fernet
import requests
from django.db import models

class Reporte(models.Model):
    id = models.AutoField(primary_key=True)
    facturas = models.CharField(max_length=255)

    def obtener_facturas(self, id_colegio,key):
        url = "http://127.0.0.1:8001/facturas/"
        params = {'idColegio': id_colegio}

        response = requests.get(url, params=params)

        if response.status_code == 200:
            facturas = response.json()
            # Pass the key here to avoid creating new files
            self.generar_csv_encriptado(facturas, id_colegio,key)
        else:
            raise Exception("Error al obtener facturas")

    def generar_csv_encriptado(self, facturas, id_colegio, key):
        # Use the passed encryption key
        cipher_suite = Fernet(key)

        output_dir = 'reportes/reportesCsv'
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        archivo_csv = os.path.join(output_dir, f"reporte_{id_colegio}.csv")

        # Create the CSV file with the invoices
        with open(archivo_csv, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['ID', 'Tipo', 'Precio', 'Fecha Pago', 'ID Colegio'])
            for factura in facturas:
                writer.writerow([factura['id'], factura['tipo'], factura['precio'], factura['fechaPago'], factura['idColegio']])

        # Encrypt the CSV file
        with open(archivo_csv, 'rb') as file:
            file_data = file.read()
            encrypted_data = cipher_suite.encrypt(file_data)

        # Save the encrypted file
        archivo_encriptado = archivo_csv + '.enc'
        with open(archivo_encriptado, 'wb') as file:
            file.write(encrypted_data)

        # Delete the original unencrypted CSV file
        os.remove(archivo_csv)

        print(f"Encrypted CSV saved as: {archivo_encriptado}")
