from django.contrib import admin
from .models import Forum, Post, Comment, User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import RegisterForm

admin.site.register(Forum)
admin.site.register(Post)
admin.site.register(Comment)

class UserAdmin(BaseUserAdmin):
    add_form = RegisterForm
    list_display = ('username', 'password', 'is_superuser')
    list_filter = ('is_superuser',)
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Permissions', {'fields': ('is_superuser', 'is_staff', 'groups', 'user_permissions')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2')}
         ),
    )
    search_fields = ('username',)
    ordering = ('username',)
    filter_horizontal = ()

admin.site.register(User, UserAdmin)