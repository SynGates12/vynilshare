# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from usuaris.models import Perfil
from django.contrib.auth.models import User
# Create your models here.

class Oferta_disc (models.Model):
    titol=models.CharField(max_length=120,)
    grup=models.CharField(max_length=120,)
    anny=models.IntegerField()
    genere=models.CharField(max_length=50,)
    preu=models.IntegerField()
    estat = models.CharField( max_length=20,default="",)
    descripcio= models.CharField( max_length=300, default="", blank=True)
    data_pujada=models.DateField( auto_now_add=True)
    usuari_venedor=models.ForeignKey('usuaris.Perfil',on_delete=models.SET_NULL,blank=True, null=True,related_name="discos_oferta")
    usuari_comprador=models.ForeignKey('usuaris.Perfil',on_delete=models.SET_NULL,blank=True, null=True, related_name="discos_comprats")
    venut=models.BooleanField(default=False, editable=False)
    visible = models.BooleanField( default=True, editable=False )
    
    image = models.ImageField(upload_to='discos',
                              blank=True)