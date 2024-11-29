from django.urls import path
from . import views

urlpatterns = [
    path('generar-csv/', views.generar_csv_view, name='generar_csv'),
]
