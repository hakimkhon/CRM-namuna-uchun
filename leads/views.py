from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from . import models
from .forms import * 

def leads_list(request):
  leads = models.Lead.objects.all()
  context = {
    "leads": leads,
  }
  return render(request, "leads_list.html", context)
    
def leads_detail(request, pk):
  lead = get_object_or_404(models.Lead, id=pk)
  context = {
    "lead": lead
  }
  return render(request, 'details.html', context)

def create(request):
  form = LeadModelForm()
  if request.method == "POST":
    # print('malumot qabul qilindi')
    form = LeadModelForm(request.POST)
    if form.is_valid():
      form.save()
      # print(form.cleaned_data)
      # fristName = form.cleaned_data['fristName']
      # lastName = form.cleaned_data['lastName']
      # age = form.cleaned_data['age']
      # agent = models.Agent.objects.first()
      # models.Lead.objects.create(
      #   fristName = fristName,
      #   lastName = lastName,
      #   age = age,
      #   agent = agent
      # )
      return redirect("/leads")
  context = {
    'forms': form
  }
  return render(request, 'create.html', context)