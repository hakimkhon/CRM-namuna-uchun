from django import forms
from django.forms import fields
from .models import Lead

class LeadModelForm(forms.ModelForm):
  class Meta:
    model =Lead
    fields = (
      "fristName",
      "lastName",
      "age",
      "agent"
    )

class LeadForm(forms.Form):
  fristName = forms.CharField(max_length=20)
  lastName = forms.CharField(max_length=20)
  age = forms.IntegerField(min_value=0)
  # email = forms.EmailField(max_length=50)