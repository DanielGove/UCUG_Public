from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import Announcement, Session

admin.site.register(Session)
admin.site.register(Announcement)
