from django.db import models

class Departement(models.Model):
    nom_dprt=models.CharField(max_length=50)
    description=models.CharField(max_length=1000)

    def __str__(self):
        return(self.nom_dprt)


class Medecin(models.Model):
    nom_med=models.CharField(max_length=50)
    prenom_med=models.CharField(max_length=50)
    specialite=models.CharField(max_length=50)
    num_tel_med=models.IntegerField()
    Departement=models.ForeignKey(Departement,on_delete=models.CASCADE)

    def __str__(self):
        return(self.nom_med)


class Patient(models.Model):
    nom_patient=models.CharField(max_length=50)
    prenom_patient=models.CharField(max_length=50)
    NSS = models.IntegerField()
    Adresse=models.CharField(max_length=50)
    num_tel_patient=models.IntegerField()
    date_naissance=models.CharField(max_length=50)

    def __str__(self):
        return(self.nom_patient)


class Dossier_Medical(models.Model):
    Traitement_medical=models.CharField(max_length=1000)
    prescriptions=models.CharField(max_length=50)

    Dpt=models.ForeignKey(Departement,on_delete=models.CASCADE)
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE)

    def __str__(self):
        return(self.prescriptions)


class RDV(models.Model):
    date=models.CharField(max_length=100)
    heure=models.CharField(max_length=50)
    statut=models.CharField(max_length=50)

    Medecin=models.ForeignKey(Medecin,on_delete=models.CASCADE)
    Patient=models.ForeignKey(Patient,on_delete=models.CASCADE)

    def __str__(self):
        return(self.date)