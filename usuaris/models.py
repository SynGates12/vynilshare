from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.

class Perfil (models.Model):
    localitat=models.CharField(max_length=50)
    CP = models.IntegerField()
    valoracio=models.IntegerField()
    # 1 to 1 - model User
    usuari = models.OneToOneField( User )
    
    
    
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
                                nom=instance.username,
                                usuari=instance,
                            )
        instance.refresh_from_db()

post_save.connect(post_save_user, sender=User)

#@receiver(post_save, sender=User)
#def create_user_profile(sender, instance, created, **kwargs):
#    if created:
#        Profile.objects.create(user=instance)


#@receiver(post_save, sender=User)
#def save_user_profile(sender, instance, **kwargs):
#    instance.profile.save()
#    