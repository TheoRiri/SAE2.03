# Generated by Django 4.2.1 on 2023-06-07 00:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectApp', '0008_alter_machine_maintenancedate'),
    ]

    operations = [
        migrations.AddField(
            model_name='machine',
            name='etat',
            field=models.CharField(choices=[('en_ligne', 'En ligne'), ('hors_ligne', 'Hors ligne')], default='hors_ligne', max_length=20),
        ),
        migrations.AlterField(
            model_name='machine',
            name='maintenanceDate',
            field=models.DateField(default=datetime.datetime(2023, 6, 7, 2, 45, 15, 507593)),
        ),
    ]
