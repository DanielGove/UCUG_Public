from django.shortcuts import render, redirect
from django.http import HttpResponse

from UCUG.models import record_session
from UCUG.models import Announcement, Forum

def home(request):
    record_session(request)

    announcements = Announcement.objects.all()
    forums = Forum.objects.all()

    return render(request=request, template_name="home.html",
                context = {"announcements": announcements,
                            "forums": forums})

def create_announcement(request):
    # Check if the user can make announcements
    if not request.user.has_perm("add_announcement"): return HttpResponse("Nice try!")
    
    announcement = Announcement(title=request.POST["title"],
                                content=request.POST["content"],
                                author=request.user)
    announcement.save()

    return redirect("/home")

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

    return HttpResponse("Hello")