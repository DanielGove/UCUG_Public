from UCUG.models import record_session
from django.shortcuts import render

from UCUG.models import Announcement, Forum

def home(request):
    record_session(request)

    announcements = Announcement.objects.all()
    forums = Forum.objects.all()

    return render(request=request, template_name="home.html",
                context = {"announcements": announcements,
                            "forums": forums})