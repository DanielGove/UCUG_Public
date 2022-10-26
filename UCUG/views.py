from django.shortcuts import render, redirect
from django.http import HttpResponse

from UCUG.models import record_session
from UCUG.models import Announcement, Forum, User

from django.core import serializers
import json

def home(request):
    record_session(request)

    announcements = Announcement.objects.all()
    forums = Forum.objects.all()

    announcements_json = serializers.serialize("json", announcements)

    return render(request=request, template_name="home.html",
                context = {"announcements": announcements,
                            "forums": forums,
                            "announcement_data": announcements_json})

def create_announcement(request):
    # Check if the user can make announcements
    if not request.user.has_perm("add_announcement"): return HttpResponse("Nice try!")

    announcement = Announcement(title=request.POST["title"],
                                content=request.POST["content"],
                                author=request.user)
    announcement.save()

    # Return new announcement data to be rendered.
    serialized_announcement = serializers.serialize("json", [announcement])

    author_data = User.objects.filter(id=announcement.author.id)
    serialized_author = serializers.serialize("json", list(author_data), fields=('id', 'username', 'is_superuser', 'is_staff'))

    return HttpResponse(json.dumps([serialized_announcement, serialized_author]))

def delete_announcement(request, id):
    if not request.user.has_perm("delete_announcement"): return HttpResponse("Nice try!")

    announcement = Announcement.objects.get(id=id)
    announcement.delete()
    return HttpResponse("Sucessfully deleted announcement {}".format(id))

def create_forum(request):
    # Check if the user can make forums
    if not request.user.has_perm("add_forum"): return HttpResponse("Nice try!")

    forum = Forum(title=request.POST["title"],
                    description=request.POST["description"],
                    owner=request.user)
    forum.save()

    # Return new forum data to be rendered.
    serialized_forum = serializers.serialize("json", [forum])

    owner_data = User.objects.filter(id=forum.owner.id)
    serialized_owner = serializers.serialize("json", list(owner_data), fields=('id', 'username', 'is_superuser', 'is_staff'))

    return HttpResponse(json.dumps([serialized_forum, serialized_owner]))