from django.urls import path
from leads.views import *

app_name = "leads"

urlpatterns = [
    path('', ListsView.as_view(), name='listlar'),
    path('<int:pk>/', LeadDetailView.as_view(), name='detallar'),
    path('<int:pk>/update_detail', lead_update, name="update"),
    path('<int:pk>/delete', leadDelete, name="delete"),
    path('create-leads/', LeadCreateView.as_view(), name="lead-create")
]
 