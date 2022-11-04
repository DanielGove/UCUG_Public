from django.http import HttpResponse
from django.shortcuts import render
import json

from UCUG.models import record_session
from ucug_forum.models import Forum

def create_forum(request):
    # Check if the user can make forums
    if not request.user.has_perm("add_forum"):
        record_session(request, "NO_AUTH")
        return HttpResponse("Nice try!")

    forum = Forum(title=request.POST["title"],
                    description=request.POST["description"],
                    owner=request.user)
    forum.save()

    # Return new forum data to be rendered.
    forum_data = forum.public_data()
    owner_data = forum.owner.public_data()

    return HttpResponse(json.dumps([forum_data, owner_data]))

def forum_feed(request, title):
    record_session(request)
    template_name = "forum_feed.html"
    context = {
        "forum" : Forum.objects.get(title=title)
    }
    return render(request, template_name, context=context)