from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from ucug_auth.models import User


# Django automatically creates an integer id primary key.
class Forum(models.Model):
    created_UTC = models.DateTimeField(auto_now_add=True)
    updated_UTC = models.DateTimeField(auto_now=True)

    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    title = models.CharField(max_length=64, default="Null")
    description = models.CharField(max_length=256)

    def public_data(self):
        data = {
            "id" : self.id,
            "title" : self.title,
            "description" : self.description,
            "owner" : self.owner.id,
        }
        return data

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

    def public_data(self):
        data = {
            "id" : self.id,
            "title" : self.title,
            "content" : self.content,
            "owner" : self.owner,
            "forum" : self.parent_forum,
        }
        return data

    def __str__(self):
        return self.title

class Comment(models.Model):
    content = models.TextField()

    created_UTC = models.DateTimeField(auto_now_add=True)
    updated_UTC = models.DateTimeField(auto_now=True)

    parent_post = models.ForeignKey(Post, null=True, blank=True, on_delete=models.SET_NULL)
    parent_comment = models.ForeignKey("Comment", null=True, blank=True, on_delete=models.SET_NULL)

    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    ip_owner = models.GenericIPAddressField(null=True)

    def public_data(self):
        data = {
            "id" : self.id,
            "content" : self.content,
            "owner" : self.owner,
            "post" : self.parent
        }
        return data

    def __str__(self):
        return self.content[:24]