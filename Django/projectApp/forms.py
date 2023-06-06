from django import forms
from django.core.exceptions import ValidationError
from projectApp.models import Machine
from .models import Personnel

class AddMachineForm(forms.Form):

    TYPE = (
       ('PC', ('PC - Run windows')),
       ('Mac', ('Mac - Run MacOS')),
       ('Serveur', ('Serveur - Simple Server to deploy virtual machines')),
       ('Switch', ('Switch - To maintains and connect servers')),
   )
    nom = forms.CharField(required=True, label='Nom de la machine')
    mach = forms.ChoiceField(choices=TYPE, required=False)
    utilisateur = forms.ModelChoiceField(queryset=Personnel.objects.all(), required=False, label='Utilisateur')

    def clean_nom(self):
        data = self.cleaned_data["nom"]
        if len(data) > 60:
            raise ValidationError(("Erreur de format pour le champ nom"))

        return data

class AddPersonnelForm(forms.Form):

    nom= forms.CharField(required=True, label='Nom du Personnel')

    def clean_nom(self):
        data = self.cleaned_data["nom"]
        if len(data) > 60:
            raise ValidationError(("Erreur de format pour le champ nom"))

        return data

class DeleteMachineForm(forms.Form):
   machine = forms.ModelChoiceField(queryset=Machine.objects.all(), label='Machine à supprimer')
