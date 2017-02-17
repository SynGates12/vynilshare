from django.conf.urls import url
from . import views

app_name='discos'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<id_oferta_disc>\d+)/$', views.vinil_informacio,name='vinil_informacio'),

]