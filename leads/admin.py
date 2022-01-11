from django.contrib import admin

from .models import Lead, User, Agent, UserProfil, Userlar

admin.site.register(Lead)
admin.site.register(User)
admin.site.register(UserProfil)
admin.site.register(Agent)
admin.site.register(Userlar)
