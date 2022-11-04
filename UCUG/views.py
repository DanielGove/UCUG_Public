from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core import serializers
import json

from UCUG.models import record_session
from UCUG.models import Announcement, User
from ucug_forum.models import Forum


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
    announcement_data = announcement.public_data()
    author_data = announcement.author.public_data()

    return HttpResponse(json.dumps([announcement_data, author_data]))

def edit_announcement(request):
    # Check if the user can edit announcements
    if not request.user.has_perm("edit_announcement"): return HttpResponse("Nice try!")

    announcement = Announcement.objects.get(id=request.POST["id"])
    announcement.title = request.POST["title"]
    announcement.content = request.POST["content"]
    announcement.save()

    return HttpResponse("Announcement {} edited.".format(announcement.id))

def delete_announcement(request, id):
    if not request.user.has_perm("delete_announcement"): return HttpResponse("Nice try!")

    announcement = Announcement.objects.get(id=id)
    announcement.delete()
    return HttpResponse("Sucessfully deleted announcement {}".format(id))
