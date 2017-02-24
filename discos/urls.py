from django.conf.urls import url
from . import views

app_name='discos'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^recomenats/$', views.recomenats, name='recomenats'),
    url(r'^(?P<id_oferta_disc>\d+)/$', views.vinil_informacio,name='vinil_informacio'),
    url(r'^contacte', views.contacte, name="contacte"),
    url(r'^cercador/$', views.cercador, name="cercador"),
 #   url(r'^search', views.search, name="search"),
    url(r'^menu/(?P<usuari_id>\d+)/afegir_disc/$', views.afegir_disc, name="afegir_disc"),
    url(r'^vinil_informacio/(?P<oferta_disc_id>\d+)$', views.vinil_informacio, name="vinil_informacio"),
    url(r'^editar_disc/$', views.editar_disc, name="editar_disc"),
    url(r'^discos/$', views.discos_venuts,name="discos_venuts"),
    url(r'^ultims/$', views.ultims, name='ultims'),
]