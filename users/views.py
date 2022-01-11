from django.views import generic
# from django.contrib.auth.mixins import LoginRequiredMixin
from leads.models import Userlar
# LoginRequiredMixin, 
class UserListView(generic.ListView):
  template_name = "users/users.html"

  def get_queryset(self):
      return Userlar.objects.all()