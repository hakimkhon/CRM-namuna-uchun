from django.urls import path
from leads.views import *

app_name = "leads"

urlpatterns = [
    path('', ListsView.as_view(), name='listlar'),
    path('<int:pk>/', LeadDetailView.as_view(), name='detallar'),
    path('<int:pk>/update_detail', LeadUpdateView.as_view(), name="update"),
    path('<int:pk>/delete', LeadDeleteView.as_view(), name="delete"),
    path('create-leads/', LeadCreateView.as_view(), name="lead-create")
]
 