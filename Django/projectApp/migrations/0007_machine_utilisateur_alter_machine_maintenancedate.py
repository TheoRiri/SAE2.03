# Generated by Django 4.2.1 on 2023-06-06 20:15

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projectApp', '0006_alter_machine_mach_alter_machine_maintenancedate'),
    ]

    operations = [
        migrations.AddField(
            model_name='machine',
            name='utilisateur',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='projectApp.personnel'),
        ),
        migrations.AlterField(
            model_name='machine',
            name='maintenanceDate',
            field=models.DateField(default=datetime.datetime(2023, 6, 6, 22, 15, 18, 982139)),
        ),
    ]