# Generated by Django 3.2.6 on 2024-11-29 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('tipo', models.CharField(max_length=100)),
                ('precio', models.IntegerField()),
                ('fechaPago', models.DateField()),
                ('idColegio', models.IntegerField()),
            ],
        ),
    ]
