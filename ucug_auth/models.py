from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin

from django.utils.translation import gettext_lazy as _

class UserManager(BaseUserManager):
    user_in_migration = True

    def create_user(self, username, password=None, **other):
        if not username:
            raise ValueError(_('The Username must be set.'))
        user = self.model(username=username, **other)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password, **other):
        other.setdefault('is_staff', True)
        other.setdefault('is_superuser', True)

        if other.get('is_superuser') == False:
            raise ValueError('Superuser must have is_superuser=True')
        if other.get('is_staff') == False:
            raise ValueError('Superuser must have is_staff=True')
        return self.create_user(username, password, **other)

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(_('username'), max_length=64, unique=True, null=True)
    is_superuser = models.BooleanField(_('superuser'), default=False)
    is_staff = models.BooleanField(_('staff'), default=False)

    description = models.CharField(_('description'), max_length=255, 
                                    default='', blank=True)
    profile_picture = models.ImageField(_('picture'), default="default.png",
                                        upload_to="profile_pics", blank=True)

    joined = models.DateTimeField(_('joined'), auto_now_add=True)
    last_active = models.DateTimeField(_('last_active'), auto_now=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    def public_data(self):
        data = {
            "id" : self.id,
            "username" : self.username,
            "url" : "/profile/{}".format(self.username),
            "is_superuser" : self.is_superuser,
            "is_staff" : self.is_staff,
        }
        return data

    def __str__(self):
        return self.username