from django.http import HttpResponse
from django.shortcuts import render
import json

from UCUG.models import record_session
from ucug_forum.models import Forum, Post, get_posts

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

def edit_forum(request):
    if not request.user.has_perm("edit_forum"):
        record_session(request, "NO_AUTH")
        HttpResponse("Nice Try!")
    
    forum = Forum.objects.get(id=request.POST["id"])
    forum.title = request.POST["title"]
    forum.description = request.POST["description"]
    forum.save()

    print(forum.public_data())

    return HttpResponse("Forum {}: \"{}\" edited.".format(forum.id, forum.title))

def create_post(request):
    if request.user:
        owner = request.user
    else:
        owner = None

    # Get the poster's IP Address
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')

    # Find parent forum
    parent_forum = Forum.objects.get(id=request.POST["forum"])

    post = Post(title=request.POST["title"],
                content=request.POST["content"],
                parent_forum=parent_forum,
                owner=owner,
                ip_owner=ip)
    post.save()

    post_data = post.public_data()
    return HttpResponse(json.dumps([post_data]))

def forum_feed(request, title=None, id=None):
    record_session(request)
    template_name = "forum_feed.html"

    try:
        if id:
            forum = Forum.objects.get(id=id)
        elif title:
            forum = Forum.objects.get(title=title)
        else:
            raise Exception
    except:
        print("Invalid forum request.")
        return HttpResponse("NOT FOUND "
            "This forum might have a new name, "
            "try looking on the "
            "<a href='/home'>home page</a>.")

    forum_data = forum.public_data()
    raw_post_data = get_posts(forum=forum_data["id"])
    context = {
        "forum" : forum_data,
        "posts" : [post.public_data() for post in raw_post_data],
    }
    return render(request, template_name, context=context)