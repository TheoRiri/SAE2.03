# Generated by Django 4.2.1 on 2023-06-05 22:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectApp', '0004_alter_machine_maintenancedate_alter_personnel_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machine',
            name='maintenanceDate',
            field=models.DateField(default=datetime.datetime(2023, 6, 6, 0, 39, 3, 258513)),
        ),
    ]
