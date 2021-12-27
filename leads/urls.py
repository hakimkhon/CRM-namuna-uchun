from django.urls import path
from leads.views import *

app_name = "leads"

urlpatterns = [
    path('', leads_list),
    path('<int:pk>/', leads_detail),
    path('<int:pk>/update', lead_update),
    path('<int:pk>/delete', leadDelete),
    path('create/', create)
]
