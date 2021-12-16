from django.urls import path
from leads.views import *

app_name = "leads"

urlpatterns = [
    path('', leads_list),
    path('<pk>/', leads_detail)
]
