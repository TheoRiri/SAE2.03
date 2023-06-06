from django.db import models
from django.core.validators import MaxValueValidator
from datetime import datetime


# Create your models here.

class Personnel(models.Model):
    id = models.AutoField(primary_key=True, editable=True, validators=[MaxValueValidator(9999999999999)])
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    
    def __str__(self):
        return str(self.id) + " -> " + self.nom + " " + self.prenom

    def get_name(self):
        return str(self.id) + " " + self.nom + " " + self.prenom


class Machine(models.Model):

    TYPE_CHOICES = (
        ('PC', 'PC - Run Windows'),
        ('Mac', 'Mac - Run MacOS'),
        ('Serveur', 'Serveur - Simple Server to deploy virtual machines'),
        ('Switch', 'Switch - To maintain and connect servers'),
    )
    id = models.AutoField(
                        primary_key=True, 
                        editable=False)
    nom = models.CharField(
                        max_length= 6)

    def __str__ (self):
        return str(self.id) + "->" + self.nom

    def get_name(self):
        return str(self.id) + "" + self.nom

    maintenanceDate=models.DateField(default=datetime.now())

    mach=models.CharField(max_length=32, choices=TYPE_CHOICES, default='PC')
    utilisateur = models.ForeignKey(Personnel, on_delete=models.SET_NULL, null=True, blank=True)

