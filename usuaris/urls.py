from django.conf.urls import url
from . import views

app_name='usuaris'

urlpatterns = [
    url(r'^creacio_usuari/$',views.Crear_usuari,name="creacio_usuari"),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.login, name='logout'),
]
