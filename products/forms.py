from django import forms
from django.forms import ModelForm
from .models import User

class Register(ModelForm):
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)
    class Meta: 
        model = User 
        fields = "__all__"
