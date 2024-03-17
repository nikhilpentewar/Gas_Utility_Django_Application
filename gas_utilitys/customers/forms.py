from django import forms
from .models import ServiceRequest
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User

# from django.contrib.auth.forms import AuthenticationForm
# from django.forms.widgets import PasswordInput, TextInput

# class CreateUserForm(UserCreationForm):

#     class Meta:

#         model = User
#         fields = ['username',  'password1', 'password2']

# class LoginForm(AuthenticationForm):

#     username = forms.CharField(widget=TextInput())
#     password = forms.CharField(widget=PasswordInput())

class ServiceRequestForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ['request_type', 'details']

