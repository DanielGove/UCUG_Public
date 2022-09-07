#import uuid
from django.db import models 
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

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

class User(AbstractBaseUser):
    username = models.CharField(_('username'), max_length=64, unique=True, null=True)
    is_superuser = models.BooleanField(_('is_superuser'), default=False)
    is_staff = models.BooleanField(default=False)

    joined = models.DateTimeField(_('joined'), auto_now_add=True)
    last_active = models.DateTimeField(_('last_active'), auto_now=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    def __str__(self):
        return self.username

# Django automatically creates an integer id primary key.
class Forum(models.Model):
    created_UTC = models.DateTimeField(auto_now_add=True)
    updated_UTC = models.DateTimeField(auto_now=True)

    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    title = models.CharField(max_length=64, default="Null")
    description = models.CharField(max_length=256)

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=64, default="Null")
    content = models.TextField()

    created_UTC = models.DateTimeField(auto_now_add=True)
    updated_UTC = models.DateTimeField(auto_now=True)

    parent_forum = models.ForeignKey(Forum, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    ip_owner = models.GenericIPAddressField(null=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    content = models.TextField()

    created_UTC = models.DateTimeField(auto_now_add=True)
    updated_UTC = models.DateTimeField(auto_now=True)

    # A comment will either be to a post or another comment.
    # reference_type tells us on which table to use the reference_id.
    reference_type = models.ForeignKey(ContentType, on_delete=models.SET_NULL, null=True)
    reference_id = models.PositiveIntegerField()

    parent_post = GenericForeignKey('reference_type', 'reference_id')
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    ip_owner = models.GenericIPAddressField(null=True)

    def __str__(self):
        return self.content[:24]

class Session(models.Model):
    time_UTC = models.DateTimeField(auto_now_add=True)
    ip = models.GenericIPAddressField(null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    method = models.CharField(max_length=8)
    route = models.CharField(max_length=32)

class private_message(models.Model):
    created_UTC = models.DateTimeField(auto_now_add=True)

    is_read = models.BooleanField(default=False)

    from_user = models.ForeignKey(User, related_name='%(class)s_from_user', on_delete=models.SET_NULL, null=True)
    to_user = models.ForeignKey(User, related_name='%(class)s_to_user', on_delete=models.SET_NULL, null=True)

    subject = models.CharField(max_length=32)
    message = models.TextField(null=True)

from UCUG.settings import DEBUG
def record_session(request):
    # When hosting on pythonanywhere (DEBUG=False) this is where the client IP is stored.
    # Using the regular method would return the ip of a pythonanywhere server.
    if DEBUG == False:
        ip = request.headers['X-Real-IP']
    else:
        ip = request.META.get('REMOTE_ADDR')

    # If user is not logged in then request.user is a special type "AnonymousUser" which cannot be referenced
    # properly in the sessions table. Must be set to none.
    if isinstance(request.user, User):
        user = request.user
    else:
        user=None
    session = Session(ip=ip,
                      method=request.method,
                      route=request.path,
                      user=user)
    return session.save()

# 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