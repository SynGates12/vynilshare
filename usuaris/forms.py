from django import forms
from django.conf import settings
from .models import Perfil
from django.contrib.auth.models import User
from django.forms import ModelForm


class LoginForm(forms.Form):
    username=forms.CharField(label="Nom usuari",
                             max_length=200,
                             help_text="Nom d'usuari.")
    password=forms.CharField(label="Paraula de pas",
                             max_length=24,
                             help_text="Paraula de pas per accedir a sistema.",
                             widget=forms.PasswordInput(),
                            )
                            
class nou_usuari_form(forms.Form):
    email=forms.EmailField(label="Correu",
                             max_length=200,
                             help_text="Correu .")
    password=forms.CharField(label="Paraula de pas",
                             max_length=24,
                             help_text="Paraula de pas per accedir a sistema.",
                             widget=forms.PasswordInput(),
                            )

class MissatgeForm(forms.Form):
    text=forms.CharField(label="descripcio",widget=forms.Textarea)
    data_lectura=forms.DateField(label="data_lectura",input_formats=settings.DATE_INPUT_FORMATS)
    