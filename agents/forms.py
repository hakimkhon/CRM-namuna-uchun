from django import forms
from django.db.models import fields
from leads.models import Agent


class AgentModelForm(forms.ModelForm):
  class Meta:
    model = Agent
    fields = (
      'user',
    )
