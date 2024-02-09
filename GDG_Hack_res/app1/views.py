from asyncio.windows_events import NULL
from uuid import RFC_4122
from django.shortcuts import render
from .models import Challenge, Submission, Judge, Critic
from django.db.models import Q
from django.db.models import fields
from django.db import connection

def display_sub(request):
    submission=Submission.objects.all()
    return render(request,"disp_sub.html",{"S1":submission})
def display_criti(request):
    criti=Critic.objects.all()
    return render(request,"disp_criti.html",{"CR1":criti})
