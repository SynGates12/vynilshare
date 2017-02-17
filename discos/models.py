from __future__ import unicode_literals

from django.db import models
from usuaris.models import Perfil

# Create your models here.

class Oferta_disc (models.Model):
    titol=models.CharField(max_length=120,)
    grup=models.CharField(max_length=120,)
    anny=models.DateField()
    genere=models.CharField(max_length=50,)
    preu=models.IntegerField()
    data_pujada=models.DateField()
    usuari_venedor=models.ForeignKey('usuaris.Perfil',on_delete=models.SET_NULL,blank=True, null=True,related_name="usuari_venedor")
    usuari_comprador=models.ForeignKey('usuaris.Perfil',on_delete=models.SET_NULL,blank=True, null=True, related_name="usuari_comprador")
    venut=models.BooleanField(default=False, editable=False)
    visible = models.BooleanField( default=True, editable=False )