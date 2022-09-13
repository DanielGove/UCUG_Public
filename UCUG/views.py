from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.edit import FormView
from django.views import View
from numpy import record
from UCUG.models import record_session
from .forms import RegisterForm
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

    def get(self, request):
        record_session(request)
        return render(request, self.template_name,
            context={'form': self.form_class()})

    def post(self, request):
        record_session(request)
        user_form = self.form_class(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            print("REGISTRATION FORM IS VALID FOR NEW USER {}".format(user))
            login(request, user)
            return redirect(self.success_url)
        else:
            print("REGISTRATION FORM IS INVALID")
            return render(request, self.template_name,
                context={'form': self.form_class()})

    def is_valid(self, form):
        user = form.save(commit=False)
        user.save()
        login(self.request, user)
        record_session(self.request)
        if user is not None:
            return HttpResponseRedirect(self.success_url)

        return super().form_valid(form)

class LoginView(View):
    template_name = 'login.html'
    success_url = '/home'

    def get(self, request):
        record_session(request)
        return render(request, self.template_name)    

    def post(self, request):
        record_session(request)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(self.success_url)
        return render(request, self.template_name)

def logout_request(request):
    record_session(request)

    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect("/home")

def RequestProfile(request):
    record_session(request)

    # Show the user profile. user id is in request.id
    # if user id is the request id, let the user edit their profile.
    return render(request=request, template_name="profile.html")
