from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import CustomUser
from django import forms

class registration(UserCreationForm):
    gender = forms.ChoiceField( choices=CustomUser.genderchoice, widget=forms.RadioSelect)
    class Meta:
        model = CustomUser
        fields = ['username' , 'gender','email' , 'password1', 'password2']