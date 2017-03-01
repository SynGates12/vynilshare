from django.conf.urls import url
from . import views

app_name='discos'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^cercador/$', views.cercador, name="cercador"),
    url(r'^ultims/$', views.ultims, name='ultims'),
    url(r'^recomanats/$', views.recomanats, name='recomanats'),
    url(r'^contacte', views.contacte, name="contacte"),
    url(r'^menu/(?P<usuari_id>\d+)/afegir_disc/$', views.afegir_disc, name="afegir_disc"),
    url(r'(?P<oferta_disc_id>\d+)/eliminar_disc/$', views.eliminar_disc, name="eliminar_disc"),
    url(r'^usuari_informacio/(?P<usuari_id>\d+)/$', views.usuari_informacio,name="usuari_informacio"),
#   url(r'^(?P<oferta_disc_id>\d+)/$', views.vinil_informacio,name='vinil_informacio'),
    url(r'^vinil_informacio/(?P<oferta_disc_id>\d+)$', views.vinil_informacio, name="vinil_informacio"),
    url(r'^(?P<oferta_disc_id>\d+)/editar_disc/$', views.editar_disc, name="editar_disc"),
    url(r'^discos/$', views.discos_venuts,name="discos_venuts"),
    
    
]