from django.shortcuts import render
from django.http import HttpResponse

def home(requires):
  return HttpResponse("Salom Dunyo")
    
