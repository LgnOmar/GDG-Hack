from django.db.models import fields
from django import forms
from .models import Patient
from .models import Medecin
from .models import RDV,Departement

from .models import Dossier_Medical
from datetime import datetime


class PatientForm (forms.ModelForm):
    class Meta:
        model = Patient
        fields = "__all__"

    def clean_num_tel_patient(self):
        num_tel_patient = self.cleaned_data['num_tel_patient']

        if len(str(num_tel_patient)) != 10:
            raise forms.ValidationError("The phone number must have exactly 10 digits.")

        return num_tel_patient

    def clean_NSS(self):
        NSS = self.cleaned_data['NSS']
        if len(str(NSS)) != 12:
            raise forms.ValidationError("The NSS number must have exactly 12 digits.")
        return NSS


    def clean_date_naissance(self):
        date_naissance = self.cleaned_data['date_naissance']

        # Check if the date is in the format dd/mm/yyyy
        try:
            parsed_date = datetime.strptime(date_naissance, '%d/%m/%Y')
        except ValueError:
            raise forms.ValidationError("Invalid date format. Please use the format dd/mm/yyyy.")

        # Check if the date is less than the current date
        if parsed_date >= datetime.now():
            raise forms.ValidationError("Date of birth must be in the past.")

        return date_naissance

    def clean_nom_patient(self):
        nom_patient = self.cleaned_data['nom_patient']

        # Check if the name contains only alphabetic characters
        if not nom_patient.isalpha():
            raise forms.ValidationError("Le nom doit contenir uniquement des caractères alphabétiques.")

        return nom_patient

    def clean_prenom_patient(self):
        prenom_patient = self.cleaned_data['prenom_patient']

        # Check if the first name contains only alphabetic characters
        if not prenom_patient.isalpha():
            raise forms.ValidationError("Le prénom doit contenir uniquement des caractères alphabétiques.")

        return prenom_patient


class MedForm(forms.ModelForm):
    class Meta:
        model = Medecin
        fields = "__all__"

    def clean_num_tel_med(self):
        num_tel_med  = self.cleaned_data['num_tel_med']

        # Check if the phone number has exactly 10 digits
        if len(str(num_tel_med)) != 10:
            raise forms.ValidationError("Le numéro de téléphone doit avoir exactement 10 chiffres.")

        return num_tel_med

    def clean_nom_med(self):
        nom_med = self.cleaned_data['nom_med']

        # Check if the name contains only alphabetic characters
        if not nom_med.isalpha():
            raise forms.ValidationError("Le nom doit contenir uniquement des caractères alphabétiques.")

        return nom_med

    def clean_prenom_med(self):
        prenom_med = self.cleaned_data['prenom_med']

        # Check if the first name contains only alphabetic characters
        if not prenom_med.isalpha():
            raise forms.ValidationError("Le prénom doit contenir uniquement des caractères alphabétiques.")

        return prenom_med


class RDVForm(forms.ModelForm):

    STATUT_CHOICES = (
        ('confirme', 'Confirmé'),
        ('annule', 'Annulé'),
        ('reporte', 'Reporté'),
    )

    statut = forms.ChoiceField(choices=STATUT_CHOICES)

    class Meta:
        model = RDV
        fields = "__all__"


    def clean_heure(self):
        heure = self.cleaned_data['heure']

        # Check if the heure is between 8 and 17
        try:
            heure_int = int(heure)
            if heure_int < 8 or heure_int > 17:
                raise forms.ValidationError("L'heure doit être entre 8h et 17h.")
        except ValueError:
            raise forms.ValidationError("L'heure doit être un nombre entier.")

        return heure

    def clean_date(self):
        date = self.cleaned_data['date']

         #Check if the date is in the format dd/mm/yyyy
        try:
           parsed_date = datetime.strptime(date, '%d/%m/%Y')
        except ValueError:
           raise forms.ValidationError("Format de date invalide. Utilisez le format dd/mm/yyyy.")

        # Check if the date is less than the current date
       # if parsed_date >= datetime.now().date():
        #    raise forms.ValidationError("La date doit être antérieure à la date actuelle.")

        return date



class DossForm (forms.ModelForm):
    class Meta:
        model = Dossier_Medical
        fields="__all__"



# ----------------------------------------------------------NEW LINES ----------------------------------------------------------


class RDVSearchForm(forms.Form):
    date = forms.CharField(label='Date du RDV', required=False)
    heure = forms.CharField(label='Heure du RDV', required=False)

class DossierMedicalSearchForm(forms.Form):
    patient = forms.CharField(label='Nom du patient', required=False)
    departement = forms.ModelChoiceField(queryset=Departement.objects.all(), label='Département', required=False)
