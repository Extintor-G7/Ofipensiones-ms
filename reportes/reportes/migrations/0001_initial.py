# Generated by Django 3.2.6 on 2024-11-29 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reporte',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('facturas', models.CharField(max_length=255)),
            ],
        ),
    ]
