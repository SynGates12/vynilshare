# -*- coding: utf-8 -*-
from django import forms

#formulari BUSCADOR que al final no fem servir
class SearchForm(forms.Form):
    CHOICE_L = (
                ( 'TITOL', 'titol'),
                ( 'GRUP', 'grup'),
                ( 'GENERE', 'genere'),
                )
    tipus_de_recerca = forms.CharField(max_length=100,widget=forms.Select(choices=CHOICE_L),)
    text = forms.CharField(max_length=400)
    


class ContacteForm(forms.Form):
    nom = forms.CharField(max_length=50, label = 'El teu nom')
    email = forms.EmailField (label="El teu email per poder respondre't")
    missatge = forms.CharField(widget=forms.Textarea)
 
 
class DiscForm (forms.Form):
    titol = forms.CharField(max_length=120, label = 'Titol')
    grup = forms.CharField(max_length=120,label="Grup")
    anny = forms.IntegerField(label ="Any")
    GENERE_CHOICES = (
                        ( 'PROGRESSIVE', 'Progessive'),
                        ( 'ALT ROCK', 'Alt Rock'),
                        ( 'HARD ROCK', 'Hard Rock'),
                        ( 'BLUES', 'Blues'),
                        ( 'HEAVY METAL', 'Heavy Metal'),
                        ( 'DISCO', 'Disco'),
                        ( 'HIP-HOP', 'Hip-hop'),
                        ( 'FOLK', 'Folk'),
                        ( 'INDIE', 'Indie'),
                        ( 'FUNK', 'Funk'),
                        ( 'CLASSICA', 'Classica'),
                        ( 'WORLD MUSIC', 'World Music'),
                        ( 'HOUSE', 'House'),
                        ( 'ALTRES', 'Altres')
                    )
    genere=forms.CharField(label="genere",max_length=50,widget=forms.Select(choices=GENERE_CHOICES),)
    
    ESTAT_CHOICES = (
                        ( 'NOU', 'Nou'),
                        ( 'SEMI-NOU', 'Semi-nou'),
                        ( 'SEGONA MÀ', 'Segona mà'),
                    )
    estat = forms.CharField(label="estat",max_length=20,widget=forms.Select(choices=ESTAT_CHOICES),)
    preu=forms.IntegerField(label="preu")
    descripcio= forms.CharField(label="descripcio",widget=forms.Textarea)
    image = forms.ImageField(label='Selecciona un archivo')