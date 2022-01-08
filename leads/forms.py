from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField
from .models import Lead

User = get_user_model()

class  LeadModelForm(forms.ModelForm):
  class Meta:
    model =Lead
    fields = (
      "fristName",
      "lastName",
      "age",
      # "email",
      "agent"
    )

class LeadForm(forms.Form):
  fristName = forms.CharField(max_length=20)
  lastName = forms.CharField(max_length=20)
  age = forms.IntegerField(min_value=0)
  # email = forms.EmailField(max_length=50)

class NewUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",)
        field_classes = {'username': UsernameField}
