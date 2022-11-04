from UCUG.settings import DEBUG
from django.db import models

from ucug_auth.models import User


class Announcement(models.Model):
    title = models.CharField(max_length=64, null=True)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    created_UTC = models.DateTimeField(auto_now_add=True)

    def public_data(self):
        data = {
            "id" : self.id,
            "title": self.title,
            "content" : self.content,
            "author": self.author.id,
        }
        return data

class Session(models.Model):
    time_UTC = models.DateTimeField(auto_now_add=True)
    ip = models.GenericIPAddressField(null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    method = models.CharField(max_length=8)
    route = models.CharField(max_length=32)

    MESSAGES = (
        ('NONE', ''),
        ('NO_AUTH', 'NO_AUTH'),
    )
    message = models.CharField(
        max_length=16,
        choices=MESSAGES,
        default="NONE",
    )

def record_session(request, message=None):
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
                      user=user,
                      message=message if message else "NONE")
    return session.save()
