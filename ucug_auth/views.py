from django.views import View
from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse, HttpResponseRedirect
import django.contrib.messages as messages

from ucug_auth.forms import RegisterForm
from UCUG.models import record_session
from ucug_auth.models import User

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
            login(request, user)
            return redirect(self.success_url)

        return render(request, self.template_name,
                    context={'form': user_form})

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

        messages.add_message(request, messages.ERROR,
                    "Username or Password is incorrect.")
        return render(request, self.template_name)

def logout_request(request):
    record_session(request)
    logout(request)
    return redirect("/home")

def RequestProfile(request, name):
    record_session(request)

    try:
        profile = User.objects.get(username=name)
    except:
        return render(request, template_name="invalid_profile.html")

    # Show the user profile. user id is in request.id
    # if user id is the request id, let the user edit their profile.
    return render(request, template_name="profile.html",
                context={"profile": profile})

def update_profile_description(request):
    if request.method == "POST":
        description = request.POST.get("description")

        # Update the profile decription of the user who made the request.
        try:
            user = User.objects.get(username=request.user.username)
        except:
            record_session(request, "NO_AUTH")
            return HttpResponse("Nice try!")

        if description:
            user.description = description
        else:
            user.description = "No description provided."

        user.save()

        return HttpResponse(user.description)

def update_profile_image(request):
    if request.method == "POST":
        image = request.FILES.get("image")

        try:
            user = User.objects.get(username=request.user.username)
        except:
            record_session(request, "NO_AUTH")
            return HttpResponse("Nice try!")

        if image:
            user.profile_picture = image
        else:
            user.profile_picture = "default.png"
        user.save()

        return HttpResponse(user.profile_picture.url)