from django.urls import path
from . import views
from .views import rechercher_patients

urlpatterns = [
   path('list_Patient/',views.affiche_patient,name="listePatient"),
   path('list_Medecin/',views.affiche_medcin ,name="listeMedecin"),
   path('list_RDV/',views.affiche_RDV,name="listeRDV"),
   path('list_Dossier/',views.affiche_dossier,name="listeDossier"),


   path('list_Rdv_Cardiologie/',views.affiche_RDV_cardiologie,name="listeCRDV"),
   path('list_Dossier_Cardiologie/',views.affiche_Dossier_cardiologie,name="listeCDossier"),
   path('list_Medecin_Cardiologie/',views.affiche_Medecin_cardiologie,name="listeCMedecin"),
   path('list_Patient_Cardiologie/',views.affiche_Patient_cardiologie,name="listeCPatient"),


   path('list_Rdv_ORL/',views.affiche_RDV_ORL,name="listeORDV"),
   path('list_Dossier_ORL/',views.affiche_Dossier_ORL,name="listeODossier"),
   path('list_Medecin_ORL/',views.affiche_Medecin_ORL,name="listeOMedecin"),
   path('list_Patient_ORL/',views.affiche_Patient_ORL,name="listeOPatient"),


   path('list_Rdv_neurologie/',views.affiche_RDV_neurologue,name="listeNRDV"),
   path('list_Dossier_neurologie/',views.affiche_Dossier_Neurologie,name="listeNDossier"),
   path('list_Medecin_neurologie/',views.affiche_Medecin_Neurologie,name="listeNMedecin"),
   path('list_Patient_neurologie/',views.affiche_Patient_Neurologie,name="listeNPatient"),


   path('list_Rdv_Urologie/',views.affiche_RDV_Urologie,name="listeURDV"),
   path('list_Dossier_Urologie/',views.affiche_Dossier_Urologie,name="listeUDossier"),
   path('list_Medecin_Urologie/',views.affiche_Medecin_Urologie,name="listeUMedecin"),
   path('list_Patient_Urologie/',views.affiche_Patient_Urologie,name="listeUPatient"),



    path('create_patient/',views.creer_patient,name='addPatient'),
    path('create_medecin/',views.creer_medecin,name="addMedecin"),
    path('create_RDV/',views.creer_RDV,name='addRdv'),
    path('create_doss/',views.creer_doss,name="addDossier"),



    path('rechercher_patients/', views.rechercher_patients, name='rechercher_patients'),
    path('rechercher_medecins/', views.rechercher_medecins, name='rechercher_medecins'),
    path('rechercher_RDV/', views.rechercher_rdv, name='rechercher_RDV'),
    path('rechercher_dossiers_medicaux/', views.rechercher_dossiers_medicaux, name='rechercher_dossiers_medicaux'),



    path('rechercher_patients_dprt/<str:nom_dprt>/', views.rechercher_patients_dprt, name='rechercher_patients_par_departement'),
    path('rechercher_medecins_dprt/<str:nom_dprt>/', views.rechercher_medecins_dprt, name='rechercher_medecins_par_departement'),
    path('rechercher_RDV/<str:nom_dprt>/', views.rechercher_rdv_dprt, name='rechercher_rdv_par_departement'),







    path('LogIN/',views.loginIn,name="logIn"),
    path('Main_Page/',views.MainPage,name="main"),


    path('cardiologie/',views.cardiologie,name="cardiologie"),
    path('ORL/',views.ORL,name="ORL"),
    path('neurologue/',views.neurologue,name="neurologue"),
    path('Urologie/',views.Urologie,name="Urologie"),
    
    
]

