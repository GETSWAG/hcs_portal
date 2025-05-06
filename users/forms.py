from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'phone', 'apartment', 'floor', 'entrance')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'phone', 'apartment', 'floor', 'entrance')

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'})) 