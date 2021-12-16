from django.shortcuts import render
from django.shortcuts import get_object_or_404
from . import models

def leads_list(request):
  leads = models.Lead.objects.all()
  # agents = models.Agent.objects.all()
  context = {
    "leads": leads,
    # "agents": agents
  }
  return render(request, "leads_list.html", context)
    
def leads_detail(request, pk):
  # print(pk)
  lead = get_object_or_404(models.Lead, id=pk)
  # print(lead)
  return render(request, 'details.html')