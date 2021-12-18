from django import forms

class LeadForm(forms.Form):
  fristName = forms.CharField(max_length=20)
  lastName = forms.CharField(max_length=20)
  age = forms.IntegerField(min_value=0)
  email = forms.EmailField(max_length=50)