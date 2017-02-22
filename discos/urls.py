from django.conf.urls import url
from . import views

app_name='discos'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<id_oferta_disc>\d+)/$', views.vinil_informacio,name='vinil_informacio'),
    url(r'^contacte', views.contacte, name="contacte"),
    url(r'^cercador/$', views.cercador, name="cercador"),
    url(r'^afegir_disc/$', views.afegir_disc, name="afegir_disc")

]