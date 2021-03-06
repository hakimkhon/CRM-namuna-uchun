from django.contrib import admin
from django.urls import path, include
from leads.views import HomeView, SigupView
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view()),
    path('leads/', include('leads.urls', namespace="leads")),
    path('agents/', include('agents.urls', namespace="agent")),
    path('users/', include('users.urls', namespace="user")),
    path('login/', LoginView.as_view(), name='login'),
    path('signup/', SigupView.as_view(), name='signup'),
    path('logout/', LogoutView.as_view(), name='logout')
]
