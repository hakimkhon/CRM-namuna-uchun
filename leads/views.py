from django.shortcuts import render, redirect, reverse
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from . import models
from .forms import * 

class HomeView(TemplateView):
  template_name = "home.html"

class ListsView(ListView):
  template_name = "leads_list.html"
  queryset = models.Lead.objects.all() 
  context_object_name = "leads"

class LeadDetailView(DetailView):
  template_name = "details.html"
  queryset = models.Lead.objects.all() 
  context_object_name = "lead"

# def leads_list(request):
#   leads = models.Lead.objects.all()
#   context = {
#     "leads": leads,
#   }
#   return render(request, "leads_list.html", context)
    
# def leads_detail(request, pk):
#   lead = get_object_or_404(models.Lead, id=pk)
#   context = {
#     "lead": lead
#   }
#   return render(request, 'details.html', context)
class LeadCreateView(CreateView):
  template_name = "create.html"
  form_class = LeadModelForm

  def get_success_url(self):
    return reverse('leads:listlar')


# def create(request):
#   form = LeadModelForm()
#   if request.method == "POST":
#     form = LeadModelForm(request.POST)
#     if form.is_valid():
#       form.save()
#       return redirect("/leads")
#   context = {
#     'forms': form
#   }
#   return render(request, 'create.html', context)

def lead_update(request, pk):
  lead = Lead.objects.get(id = pk)
  form = LeadModelForm(instance=lead)
  if request.method == "POST":
    form = LeadModelForm(request.POST, instance=lead)
    if form.is_valid():
      form.save()
      return redirect("/leads")
  context = {
    'form': form,
    'lead': lead
  }
  return render(request, 'update.html', context)

def leadDelete(request, pk):
  lead = Lead.objects.get(id = pk)
  lead.delete()
  return redirect("/leads")


  # if request.method == "POST":
  #   form = LeadForm(request.POST)
  #   if form.is_valid():
  #     fristName = form.cleaned_data["fristName"]
  #     lastName = form.cleaned_data["lastName"]
  #     age = form.cleaned_data["age"]
  #     lead.fristName = fristName
  #     lead.lastName = lastName
  #     lead.age = age
  #     lead.save()
  #     return redirect("/leads")