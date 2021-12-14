from django.shortcuts import render
# from django.http import HttpResponse

def home(request):
  context = {
    "name": "Hakimkhon",
    "surname": "Sharifxonov"
  }
  return render(request, "main.html", context)
    
