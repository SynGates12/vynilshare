from django import forms
from .models import Perfil
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username=forms.CharField(label="Nom usuari",
                             max_length=16,
                             help_text="Nom d'usuari.")
    password=forms.CharField(label="Paraula de pas",
                             max_length=24,
                             help_text="Paraula de pas per accedir a sistema.",
                             widget=forms.PasswordInput(),
                            )