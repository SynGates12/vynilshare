from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.

class Perfil (models.Model):
    #continguts extras que volem
    localitat=models.CharField(max_length=50)
    CP = models.CharField( max_length=5, blank=True )
    valoracio=models.IntegerField(blank=True, null=True, editable=False)
   
    # 1 to 1 - model User
    usuari = models.OneToOneField( User )
    
    image = models.ImageField(upload_to='perfil', blank=True)

class Missatge (models.Model):
    data=models.DateField(auto_now_add=True)
    text=models.CharField(max_length=250,)
    data_lectura=models.DateTimeField()
    msm_from=models.ForeignKey(Perfil,on_delete=models.SET_NULL,blank=True, null=True, related_name="missatges_enviats")
    msm_to=models.ForeignKey(Perfil,on_delete=models.SET_NULL,blank=True, null=True, related_name="missatges_rebuts")
    disc=models.ForeignKey('discos.Oferta_disc' )
    


def post_save_user(sender, instance, created, **kwargs):
    if created:
        nou_perfil = Perfil.objects.create(
                    usuari=instance,
                    )
        instance.refresh_from_db()

post_save.connect(post_save_user, sender=User)
