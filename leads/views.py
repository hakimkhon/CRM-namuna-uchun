from django.shortcuts import render
# from django.http import HttpResponse
from . import models

def home(request):
  leads = models.Lead.objects.all()
  agents = models.Agent.objects.all()
  context = {
    "leads": leads,
    "agents": agents
  }
  return render(request, "main.html", context)
    
