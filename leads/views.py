from django.shortcuts import render, redirect, reverse
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
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

class LeadCreateView(CreateView):
  template_name = "leads/create.html"
  form_class = LeadModelForm
  def get_success_url(self):
    return reverse('leads:listlar')

class LeadUpdateView(UpdateView):
  template_name = "leads/update.html"
  form_class = LeadModelForm
  queryset = models.Lead.objects.all() 
  def get_success_url(self):
    return reverse('leads:listlar')

class LeadDeleteView(DeleteView):
  template_name = "leads/delete.html"
  form_class = LeadModelForm
  queryset = models.Lead.objects.all() 
  def get_success_url(self):
    return reverse('leads:listlar')
  
# def lead_update(request, pk):
#   lead = Lead.objects.get(id = pk)
#   form = LeadModelForm(instance=lead)
#   if request.method == "POST":
#     form = LeadModelForm(request.POST, instance=lead)
#     if form.is_valid():
#       form.save()
#       return redirect("/leads")
#   context = {
#     'form': form,
#     'lead': lead
#   }
#   return render(request, 'update.html', context)

# def leadDelete(request, pk):
#   lead = Lead.objects.get(id = pk)
#   lead.delete()
#   return redirect("/leads")
