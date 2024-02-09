from django.contrib import admin
from .models import Departement,Medecin,Patient,Dossier_Medical,RDV
# Register your models here.



admin.site.register(Departement)
admin.site.register(Medecin)
admin.site.register(Patient)
admin.site.register(Dossier_Medical)
admin.site.register(RDV)