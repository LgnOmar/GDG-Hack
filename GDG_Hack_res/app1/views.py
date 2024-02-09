from asyncio.windows_events import NULL
from uuid import RFC_4122
from django.shortcuts import render
from .models import Challenge, Submission, Judge, Critics, Review
from django.db.models import Q
from django.db.models import fields
from django.db import connection


def display_chall(request):
    challenge=Challenge.objects.all()
    return render(request,"disp_Chall.html",{"C1":challenge})
def display_sub(request):
    submission=Submission.objects.all()
    return render(request,"disp_sub.html",{"S1":submission})