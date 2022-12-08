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
    if request.user.is_authenticated:
        owner = request.user
    else:
        owner = None

    # Get the poster's IP Address
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')

    # Find parent forum or post
    try:
        parent_forum = Forum.objects.get(id=request.POST["p_forum"])
        parent_post = None
    except:
        parent_forum = None
        parent_post = Post.objects.get(id=request.POST["p_post"])

    post = Post(title=request.POST["title"],
                content=request.POST["content"],
                parent_forum=parent_forum,
                parent_post=parent_post,
                owner=owner,
                ip_owner=ip)
    post.save()

    post_data = post.public_data()
    return HttpResponse(json.dumps([post_data]))

def edit_post(request):
    post = Post.objects.get(id=request.POST["id"])
    if not post.owner_id == request.user.id:
        record_session(request, "NO_AUTH")
        return HttpResponse("Nice Try!")
    
    post.title = request.POST["title"]
    post.content = request.POST["content"]
    post.save()

    print(request.POST)
    return HttpResponse(json.dumps(post.public_data()))

def delete_post(request):
    post = Post.objects.get(id=request.POST["id"])
    if not post.owner_id == request.user.id:
        record_session(request, "NO_AUTH")
        return HttpResponse("Nice Try!")
    post.delete()
    return HttpResponse("Post deleted.")

def get_posts_view(request):
    raw_post_data = get_posts(
        request.GET.get("ordering"),
        request.GET.get("title"),
        request.GET.get("content"),
        request.GET.get("author"),
        request.GET.get("p_forum"),
        request.GET.get("p_post"))
    return HttpResponse(json.dumps([post.public_data() for post in raw_post_data]))

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
    raw_post_data = get_posts(p_forum=forum_data["id"])
    context = {
        "forum" : forum_data,
        "posts" : [post.public_data() for post in raw_post_data],
    }
    print(context["posts"])
    return render(request, template_name, context=context)