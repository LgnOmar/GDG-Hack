from django.urls import path
from . import views

urlpatterns = [
    path('list_Chall/',views.display_chall,name="listChall"),
    
    
]

