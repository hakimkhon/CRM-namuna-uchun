from django.shortcuts import render
# from django.http import HttpResponse
from . import models

def home(request):
  leads = models.Lead.objects.all()
  context = {
    "leads": leads
  }
  return render(request, "main.html", context)
    
