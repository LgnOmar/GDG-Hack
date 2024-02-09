from asyncio.windows_events import NULL
from uuid import RFC_4122
from django.shortcuts import render
from .models import RDV, Departement, Dossier_Medical, Medecin, Patient
from .forms import PatientForm
from .forms import MedForm
from .forms import RDVForm
from .forms import DossForm
from django.db.models import Q
from django.db.models import fields
from django.db import connection

######################### PARTIE D AFFICHAGE ################################

def affiche_patient(request):
    patient=Patient.objects.all()
    return render(request,"listePatient.html",{"P1":patient})


def affiche_RDV_cardiologie(request):

    
    
     departement_cardiologie = Departement.objects.get(nom_dprt="Cardiologie")

   
     medecins_cardiologie = Medecin.objects.filter(Departement=departement_cardiologie)

     rdv_cardiologie = RDV.objects.filter(Medecin__in=medecins_cardiologie)


     return render(request, "listeRdvCardiologie.html", {"R": rdv_cardiologie}) 

def affiche_RDV_ORL(request):

    
    
     departement_cardiologie = Departement.objects.get(nom_dprt="ORL")

   
     medecins_cardiologie = Medecin.objects.filter(Departement=departement_cardiologie)

     rdv_cardiologie = RDV.objects.filter(Medecin__in=medecins_cardiologie)


     return render(request, "listeRdvORL.html", {"R": rdv_cardiologie}) 

def affiche_RDV_neurologue(request):

    
    
     departement_cardiologie = Departement.objects.get(nom_dprt="Neurologie")

   
     medecins_cardiologie = Medecin.objects.filter(Departement=departement_cardiologie)

     rdv_cardiologie = RDV.objects.filter(Medecin__in=medecins_cardiologie)


     return render(request, "listeRdvNeurologie.html", {"R": rdv_cardiologie})

def affiche_RDV_Urologie(request):

    
    
     departement_cardiologie = Departement.objects.get(nom_dprt="Urologie")

   
     medecins_cardiologie = Medecin.objects.filter(Departement=departement_cardiologie)

     rdv_cardiologie = RDV.objects.filter(Medecin__in=medecins_cardiologie)


     return render(request, "listeRdvUrologie.html", {"R": rdv_cardiologie}) 


def affiche_Dossier_cardiologie(request):

    
    
     departement_cardiologie = Departement.objects.get(nom_dprt="Cardiologie")

    
     dossier=Dossier_Medical.objects.filter(Dpt=departement_cardiologie)

    
     #patient=Dossier_Medical.objects.filter(patient__in=dossier)


     return render(request, "listeDossierCardiologie.html", {"D": dossier}) 


def affiche_Dossier_ORL(request):

    
    
     departement_cardiologie = Departement.objects.get(nom_dprt="ORL")

    
     dossier=Dossier_Medical.objects.filter(Dpt=departement_cardiologie)

    
     #patient=Dossier_Medical.objects.filter(patient__in=dossier)


     return render(request, "listeDossierORL.html", {"D": dossier}) 

def affiche_Dossier_Neurologie(request):

    
    
     departement_cardiologie = Departement.objects.get(nom_dprt="Neurologie")

    
     dossier=Dossier_Medical.objects.filter(Dpt=departement_cardiologie)

    
     #patient=Dossier_Medical.objects.filter(patient__in=dossier)


     return render(request, "listeDossierNeurologie.html", {"D": dossier})


def affiche_Dossier_Urologie(request):

    
    
     departement_cardiologie = Departement.objects.get(nom_dprt="Urologie")

    
     dossier=Dossier_Medical.objects.filter(Dpt=departement_cardiologie)

    
     #patient=Dossier_Medical.objects.filter(patient__in=dossier)


     return render(request, "listeDossierUrologie.html", {"D": dossier})



def affiche_Medecin_cardiologie(request):

    
    
     departement_cardiologie = Departement.objects.get(nom_dprt="Cardiologie")

   
     medecins_cardiologie = Medecin.objects.filter(Departement=departement_cardiologie)

    


     return render(request, "listeMedecinCardiologie.html", {"M": medecins_cardiologie})


def affiche_Medecin_ORL(request):

    
    
     departement_cardiologie = Departement.objects.get(nom_dprt="ORL")

   
     medecins_cardiologie = Medecin.objects.filter(Departement=departement_cardiologie)

    


     return render(request, "listeMedecinORL.html", {"M": medecins_cardiologie})

def affiche_Medecin_Neurologie(request):

    
    
     departement_cardiologie = Departement.objects.get(nom_dprt="Neurologie")

   
     medecins_cardiologie = Medecin.objects.filter(Departement=departement_cardiologie)

    


     return render(request, "listeMedecinNeurologie.html", {"M": medecins_cardiologie})

def affiche_Medecin_Urologie(request):

    
    
     departement_cardiologie = Departement.objects.get(nom_dprt="Urologie")

   
     medecins_cardiologie = Medecin.objects.filter(Departement=departement_cardiologie)

    


     return render(request, "listeMedecinUrologie.html", {"M": medecins_cardiologie}) 
 

def affiche_Patient_cardiologie(request):

    
    
    departement_cardiologie = Departement.objects.get(nom_dprt="Cardiologie")

    # Récupérer les dossiers médicaux liés au département de cardiologie
    dossiers_cardiologie = Dossier_Medical.objects.filter(Dpt=departement_cardiologie)

    # Récupérer les patients correspondant aux dossiers médicaux
      
    patients_cardiologie = [dossier.patient for dossier in dossiers_cardiologie]

    return render(request, "listePatientCardiologie.html", {"p": patients_cardiologie}) 

def affiche_Patient_ORL(request):

    
    
    departement_cardiologie = Departement.objects.get(nom_dprt="ORL")

    # Récupérer les dossiers médicaux liés au département de cardiologie
    dossiers_cardiologie = Dossier_Medical.objects.filter(Dpt=departement_cardiologie)

    # Récupérer les patients correspondant aux dossiers médicaux
      
    patients_cardiologie = [dossier.patient for dossier in dossiers_cardiologie]

    return render(request, "listePatientORL.html", {"p": patients_cardiologie}) 

def affiche_Patient_Neurologie(request):

    
    
    departement_cardiologie = Departement.objects.get(nom_dprt="Neurologie")

    # Récupérer les dossiers médicaux liés au département de cardiologie
    dossiers_cardiologie = Dossier_Medical.objects.filter(Dpt=departement_cardiologie)

    # Récupérer les patients correspondant aux dossiers médicaux
      
    patients_cardiologie = [dossier.patient for dossier in dossiers_cardiologie]

    return render(request, "listePatientNeurologie.html", {"p": patients_cardiologie}) 



def affiche_Patient_Urologie(request):

    
    
    departement_cardiologie = Departement.objects.get(nom_dprt="Urologie")

    # Récupérer les dossiers médicaux liés au département de cardiologie
    dossiers_cardiologie = Dossier_Medical.objects.filter(Dpt=departement_cardiologie)

    # Récupérer les patients correspondant aux dossiers médicaux
      
    patients_cardiologie = [dossier.patient for dossier in dossiers_cardiologie]

    return render(request, "listePatientUrologie.html", {"p": patients_cardiologie}) 







def affiche_medcin(request):
    medcin=Medecin.objects.all()
    return render(request,"listeMedecin.html",{"M1":medcin})


def affiche_RDV(request):
    rdv=RDV.objects.all()
    return render(request,"listeRDV.html",{"R1":rdv})



def affiche_dossier(request):
    dossier=Dossier_Medical.objects.all()
    return render(request,"listeDossier.html",{"D1":dossier})


def loginIn(request):
    
     return render(request,"index.html",)

def MainPage(request):
    
     return render(request,"MainPage.html",)

def cardiologie(request):
    
     return render(request,"cardiologie.html",)

def ORL(request):
    
     return render(request,"ORL.html",)

def neurologue(request):
    
     return render(request,"neurologue.html",)

def Urologie(request):
    
     return render(request,"Urologie.html",)


#################### PARTIE DE CREATION  #####################################





def creer_patient(request):
    mssg = ""

    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            nss = form.cleaned_data['NSS']

            # Vérifier si le NSS existe déjà dans la base de données
            if Patient.objects.filter(NSS=nss).exists():
                mssg = "Un patient avec ce NSS existe déjà. La création a été annulée."
            else:
                form.save()
                form = PatientForm()
                mssg = "Patient créé avec succès."

        return render(request, "create_patient.html", {"form": form, "message": mssg})
    else:
        form = PatientForm()
        mssg = "Veuillez remplir tous les champs."
        return render(request, "create_patient.html", {"form": form, "message": mssg})


def creer_medecin(request):
    mssg = ""  # Initialize the variable outside the if statements

    if request.method == 'POST':
        form = MedForm(request.POST)
        if form.is_valid():
            num_tel = form.cleaned_data['num_tel_med']

            # Vérifier si le numéro de téléphone existe déjà dans la base de données
            if Medecin.objects.filter(num_tel_med=num_tel).exists():
                mssg = "Un médecin avec ce numéro de téléphone existe déjà. La création a été annulée."
            else:
                form.save()
                form = MedForm()
                mssg = "Médecin créé avec succès."

    else:
        form = MedForm()
        mssg = "Veuillez remplir tous les champs."

    return render(request, "create_medecin.html", {"form": form, "message": mssg})


def creer_RDV(request):
    mssg = ""  # Initialize the variable outside the conditional blocks

    if request.method == 'POST':
        form = RDVForm(request.POST)
        if form.is_valid():
            
            champ1 = form.cleaned_data['heure']
            champ2 = form.cleaned_data['date']
            champ3 = form.cleaned_data['Medecin']

            existe_deja = RDV.objects.filter(heure=champ1,date=champ2,Medecin=champ3).exists()

            

            if not existe_deja:
              form.save()
              form = RDVForm()
              mssg = "done"
            else:
                mssg="RDV réservé déja"
            # return redirect("listing") # redirection vers la page de l’url: listing

    else:
        form = RDVForm()  # créer une instance de formulaire vierge
        #mssg = "veuillez remplir tous les champs"

    return render(request, "create_RDV.html", {"form": form, "message": mssg})


def creer_doss(request):
    if request.method == 'POST':
        form = DossForm(request.POST)
        if form.is_valid():
            form.save()
            form = DossForm()
            mssg="done"
            # return redirect("listing") # redirection vers la page de l’url: listing
        return render(request,"create_doss.html",{"form":form,"message":mssg})
    else:
        form = DossForm() #créer une instance de formulaire vierge
        mssg ="veuillez remplir tous les champs"
        return render(request,"create_doss.html",{"form":form,"message":mssg})


def rechercher_patients(request):
    patients = ""
    if request.method == "GET":
        query = request.GET.get('recherche')
        if query:
            # Ajoutez une condition pour rechercher par NSS en plus du nom
            patients = Patient.objects.filter(Q(nom_patient__contains=query) | Q(NSS__contains=query))
    return render(request, "search_patient.html", {"patients": patients})








# ----------------------------------------------------------NEW LINES ----------------------------------------------------------


def rechercher_medecins(request):
    medecins = ""
    if request.method == "GET":
        query = request.GET.get('recherche')
        if query:
            # Ajoutez une condition pour rechercher par la clé primaire en plus du nom
            medecins = Medecin.objects.filter(Q(nom_med__contains=query) | Q(prenom_med__contains=query))
    return render(request, "search_medecin.html", {"medecins": medecins})


def rechercher_rdv(request):
    rdvs = ""
    if request.method == "GET":
        date_query = request.GET.get('date')
        heure_query = request.GET.get('heure')

        if date_query or heure_query:
            # Utilisez Q pour combiner les conditions de recherche
            rdvs = RDV.objects.filter(
                Q(date__contains=date_query) &
                Q(heure__contains=heure_query)
            )

    return render(request, "search_rdv.html", {"rdvs": rdvs})


def rechercher_dossiers_medicaux(request):
    dossiers = ""
    departements = Departement.objects.all()

    if request.method == "GET":
        patient_query = request.GET.get('patient')
        departement_query = request.GET.get('departement')

        if patient_query or departement_query:
            # Utilisez Q pour combiner les conditions de recherche
            dossiers = Dossier_Medical.objects.filter(
                Q(patient__nom_patient__contains=patient_query) &
                Q(Dpt__nom_dprt__contains=departement_query)
            )

    return render(request, "search_dossier_medical.html", {"dossiers": dossiers, "departements": departements})


def rechercher_patients_dprt(request, nom_dprt=None):
    patients = ""

    if request.method == "GET":
        query = request.GET.get('recherche')

        if query:
            # Ajoutez une condition pour rechercher par NSS en plus du nom et par département
            if nom_dprt:
                patients = Patient.objects.filter(Q(nom_patient__contains=query) | Q(NSS__contains=query), dossier_medical__Dpt__nom_dprt=nom_dprt)
            else:
                patients = Patient.objects.filter(Q(nom_patient__contains=query) | Q(NSS__contains=query))

    return render(request, "search_patient_dprt.html", {"patients": patients})


def rechercher_medecins_dprt(request, nom_dprt=None):
    medecins = ""

    if request.method == "GET":
        query = request.GET.get('recherche')

        if query:
            # Ajoutez une condition pour rechercher par la clé primaire en plus du nom et par département
            if nom_dprt:
                medecins = Medecin.objects.filter(Q(nom_med__contains=query) | Q(prenom_med__contains=query), Departement__nom_dprt=nom_dprt)
            else:
                medecins = Medecin.objects.filter(Q(nom_med__contains=query) | Q(prenom_med__contains=query))

    return render(request, "search_medecin_dprt.html", {"medecins": medecins})


def rechercher_rdv_dprt(request, nom_dprt=None):
    rdvs = ""

    if request.method == "GET":
        date_query = request.GET.get('date')
        heure_query = request.GET.get('heure')

        if date_query or heure_query:
            # Utilisez Q pour combiner les conditions de recherche
            if nom_dprt:
                rdvs = RDV.objects.filter(
                    Q(date__contains=date_query) &
                    Q(heure__contains=heure_query) &
                    Q(Medecin__Departement__nom_dprt=nom_dprt)
                )
            else:
                rdvs = RDV.objects.filter(
                    Q(date__contains=date_query) &
                    Q(heure__contains=heure_query)
                )

    return render(request, "search_rdv_dprt.html", {"rdvs": rdvs})

