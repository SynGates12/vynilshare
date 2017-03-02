from django.conf.urls import url
from . import views

app_name='usuaris'

urlpatterns = [
    url(r'^crear/$', views.crear_usuari,name="crear_usuari"),
    url(r'^modificar/$', views.modificar_perfil,name="modificar_perfil"),
    url(r'^menu/$', views.menu_usuari,name="menu_usuari"),
    url(r'^(?P<oferta_disc_id>\d+)/crear_missatge/$', views.crear_missatge,name="crear_missatge"),
    url(r'^missatges/$', views.missatge_rebuts,name="missatge_rebuts"),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
   
]

