# Generated by Django 4.2.1 on 2023-06-05 22:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectApp', '0005_alter_machine_maintenancedate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machine',
            name='mach',
            field=models.CharField(choices=[('PC', 'PC - Run Windows'), ('Mac', 'Mac - Run MacOS'), ('Serveur', 'Serveur - Simple Server to deploy virtual machines'), ('Switch', 'Switch - To maintain and connect servers')], default='PC', max_length=32),
        ),
        migrations.AlterField(
            model_name='machine',
            name='maintenanceDate',
            field=models.DateField(default=datetime.datetime(2023, 6, 6, 0, 42, 35, 588453)),
        ),
    ]
