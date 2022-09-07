from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.edit import FormView
from UCUG.models import record_session
from .forms import RegisterForm, LoginForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.shortcuts import render, redirect

# This is the index "view"
# In order for a user to see this view, it must be mapped
# to a url in urls.py
def index(request):
    record_session(request)
    return render(request=request, template_name="header.html")

def home(request):
    record_session(request)
    return render(request=request, template_name="header.html")

class RegisterView(FormView):
    form_class = RegisterForm
    template_name = 'register.html'
    success_url = '/home'

    def form_valid(self, form):
        user = form.save(commit=False)
        user.save()
        login(self.request, user)
        record_session(self.request)
        if user is not None:
            return HttpResponseRedirect(self.success_url)

        return super().form_valid(form)

def login_request(request):
    template_name = 'login.html'
    success_url = '/home'

    if request.POST:
        print(request.POST)
        print()
        print()
        print()
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(success_url)

    return render('login.html')

def RequestProfile(request):
    record_session(request)

    # Show the user profile. user id is in request.id
    # if user id is the request id, let the user edit their profile.
    return render(request=request, template_name="profile.html")

def logout_request(request):
    record_session(request)

    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect("/home")
