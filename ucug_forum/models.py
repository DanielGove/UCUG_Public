from django.db import models
from django.db.models import Q
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
        if self.owner.is_superuser:
            owner_class = "super"
        elif self.owner.is_staff:
            owner_class = "staff"
        else:
            owner_class = "user"

        data = {
            "id" : self.id,
            "title" : self.title,
            "description" : self.description,
            "owner_id" : self.owner.id,
            "owner_name" : self.owner.username,
            "owner_class" : owner_class,
        }
        return data

    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=64, default="Null")
    content = models.TextField()

    created_UTC = models.DateTimeField(auto_now_add=True)
    updated_UTC = models.DateTimeField(auto_now=True)

    parent_forum = models.ForeignKey(Forum, on_delete=models.CASCADE, null=True)
    parent_post = models.ForeignKey('self', on_delete=models.CASCADE, null=True)

    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    ip_owner = models.GenericIPAddressField(null=True)

    def public_data(self):
        if self.owner:
            owner_name = self.owner.username
            owner_id = self.owner.id
            if self.owner.is_superuser:
                owner_class = "super"
            elif self.owner.is_staff:
                owner_class = "staff"
            else:
                owner_class = "user"
        else:
            owner_name = "Anon"
            owner_class = "user"
            owner_id = 0

        data = {
            "id" : self.id,
            "title" : self.title,
            "content" : self.content,
            "owner_id" : owner_id,
            "owner_name" : owner_name,
            "owner_class" : owner_class,
            "parent_post" : self.parent_post.title if self.parent_post else None,
            "parent_forum" : self.parent_forum.title if self.parent_forum else None,
        }
        return data

    def __str__(self):
        return self.title

# A functional abstraction for requesting posts to display.
# Parameters correspond to different query selectors on the front end.
# params of None equates to "all"
# page_number is used for pagination & iteratively rendering content.

# How many posts to display at a time.
PAGE_LENGTH = 15

def get_posts(ordering="Most Recent", title=None, content=None, author=None, p_forum=None, p_post=None, page_number=0):
    query = Q()

    # Filter by post contents
    if title and content:
        query &= Q(title__contains=title)
        query |= Q(content__icontains=content)
    elif title:
        query &= Q(title__icontains=title)
    elif content:
        query &= Q(content__icontains=content)
    
    # Filter by author
    if author:
        query &= Q(owner__username__icontains=author)

    # Filter by location
    if p_forum:
        query &= Q(parent_forum__id=p_forum)
    elif p_post:
        query &= Q(parent_post__id=p_post)

    # Make the constructed query with the wanted ordering
    if ordering == "Most Recent":
        posts = Post.objects.filter(query).order_by("-created_UTC")
    elif ordering == "Oldest":
        posts = Post.objects.filter(query).order_by("created_UTC")
    else:
        posts = Post.objects.filter(query)

    return posts

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