from UCUG.models import record_session
from django.shortcuts import render

def index(request):
    record_session(request)
    return render(request=request, template_name="header.html")

def home(request):
    record_session(request)
    return render(request=request, template_name="home.html")