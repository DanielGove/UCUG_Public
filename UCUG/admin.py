from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from ucug_auth.forms import RegisterForm
from UCUG.models import Forum, Post, Comment, Announcement, Session, private_message

admin.site.register(Forum)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Session)
admin.site.register(Announcement)
admin.site.register(private_message)