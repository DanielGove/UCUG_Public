from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

from datetime import datetime

class RegisterForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Password',
        'class': 'form-control form-control-lg'
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirm Password',
        'class': 'form-control form-control-lg'
    }))

    class Meta:
        model = User
        fields = ('username', "password1", "password2")
        widgets = {
            'username': forms.TextInput(attrs={
                'placeholder': 'Username',
                'class': 'form-control form-control-lg'
            })
        }
    
    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.joined = user.last_active = datetime.now()
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        print(user)
        return user