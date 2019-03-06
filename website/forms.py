from django.contrib.auth.models import User
from django import forms
from website.models import *

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password")

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('state',)