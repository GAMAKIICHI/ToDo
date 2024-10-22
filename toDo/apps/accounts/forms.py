from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

def customAttr(values: dict):
    return forms.CharField(widget = forms.TextInput(attrs=values))

class LoginForm(AuthenticationForm):
    username = customAttr({'placeholder':'Username'})
    password = customAttr({'placeholder':'Password', 'type':'password'})

class LogoutForm():
    pass

class SignUpForm(UserCreationForm):
    username = customAttr({'placeholder':'Username'})
    password1 = customAttr({'placeholder':'Password', 'type':'password'})
    password2 = customAttr({'placeholder':'Verify Password', 'type':'password'})