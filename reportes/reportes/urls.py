from django.urls import path
from . import views

urlpatterns = [
    path('generar-csv/', views.generar_csv_view, name='generar_csv'),
    path('generar-csv2/', views.descargar_csv_no_encriptado_view, name='generar_csv2'),
]
