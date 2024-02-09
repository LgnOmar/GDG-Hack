from django.urls import path
from . import views

urlpatterns = [
    path('list_Chall/',views.display_chall,name="listChall"),
    path('list_Sub/', views.display_sub, name="listSub"),
    path('list_Criti/', views.display_criti, name="listCriti"),

]

