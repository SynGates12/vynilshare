# -*- coding: utf-8 -*-
from django.shortcuts import render,get_object_or_404,redirect, render_to_response
from django.http import HttpResponse
from discos.models import Oferta_disc
from usuaris.models import Perfil, Missatge
from django.forms import modelform_factory
from django.db.models import Q
from .forms import SearchForm, ContacteForm
from .forms import DiscForm
from django.contrib import messages
 
# Create your views here.

def index(request):
    discos= Oferta_disc.objects.all();
    ctx={'llista_discos': discos}
    return render(request, "discos/index.html",ctx)
    
def recomenats(request):
    recomendados=Oferta_disc.objects.all().order_by('?')[:12]
    ctx={'recomana_discos': recomendados}
    return render(request, "discos/recomenats.html",ctx)
    
def vinil_informacio(request,oferta_disc_id):
    vinil = get_object_or_404(Oferta_disc,pk=oferta_disc_id)
    ctx={'vinil': vinil}
    return render(request,"discos/vinil_informacio.html",ctx)
    
def discos_venuts(request):
    venuts= request.user.perfil.discos_oferta.filter(venut=True)
   
    ctx={'venuts': venuts}
        
    return render (request, "discos/discos_venuts.html", ctx)
    

def contacte(request):
    
    if request.method =="POST":
        form=ContacteForm(request.POST)
        if form.is_valid():
            nom= form.cleaned_data['nom']
            email = form.cleaned_data['email']
            missatge=form.cleaned_data['missatge']
            form.save()
        return redirect ('discos:index')
            
    else:
        form = ContacteForm()
    
    for f in form.fields:
       form.fields[f].widget.attrs['class'] = 'formulari'
   
    form.fields['nom'].widget.attrs['placeholder']="Nom"
    form.fields['email'].widget.attrs['placeholder']="Email"
    form.fields['missatge'].widget.attrs['placeholder']="Missatge"
    form.fields['nom'].widget.attrs['required']="required"
    form.fields['email'].widget.attrs['required']="required"
    form.fields['missatge'].widget.attrs['required']="required"
    return render (request, 'discos/contacte.html', {'form': form})

    
    
def afegir_disc(request,usuari_id):
    usuari_venedor=Perfil.objects.get(id=usuari_id)
    if request.method == 'POST':
        form = DiscForm(request.POST,request.FILES)
        if form.is_valid():
           titol= form.cleaned_data['titol']
           grup = form.cleaned_data['grup']
           anny=form.cleaned_data['anny']
           genere=form.cleaned_data['genere']
           preu=form.cleaned_data['preu']
           estat=form.cleaned_data['estat']
           descripcio=form.cleaned_data['descripcio']
           image=form.cleaned_data['image']
           Oferta_disc.objects.create( titol=titol,
                                        grup=grup,
                                        anny=anny,
                                        genere=genere,
                                        preu=preu,
                                        estat=estat,
                                        descripcio=descripcio,
                                        usuari_venedor=usuari_venedor,
                                        image=image)   
           
           messages.info(request,"pujat correctament disc")
           return redirect("usuaris:menu_usuari")    
    else:
        form= DiscForm()
    for f in form.fields:
        form.fields[f].widget.attrs['class'] = 'formulari'
        
    
    return render (request, 'discos/afegir_disc.html', {'form': form})    
   

<<<<<<< HEAD
def editar_disc(request,oferta_disc_id=None):
    EditForm = modelform_factory(Oferta_disc, fields=('titol', 'grup','anny','genere','estat','descripcio','preu'))
=======
   
   
def editar_disc(request, oferta_disc_id=None):
    EditForm = modelform_factory(Oferta_disc, fields=('titol', 'grup','anny','genere','estat','descripcio','preu', 'image'))
>>>>>>> 403ef305a68b39d0d8e0e6b98e0fc39aa44c2ef1
    unEdit = Oferta_disc()
    
    if oferta_disc_id:
        unEdit = get_object_or_404(Oferta_disc, pk=oferta_disc_id)
    if request.method == 'POST':
        form = EditForm (request.POST,request.FILES, instance= unEdit)
        if form.is_valid():
           form.save()
           messages.info(request,"canviat correctament disc")
           return redirect("usuaris:menu_usuari")    
    else:
        form= EditForm (instance = unEdit)
    for f in form.fields:
        form.fields[f].widget.attrs['class'] = 'formulari'
 
    form.fields['titol'].widget.attrs['placeholder']="Titol"
    form.fields['grup'].widget.attrs['placeholder']="Grup"
    form.fields['anny'].widget.attrs['placeholder']="Any"
    form.fields['descripcio'].widget.attrs['placeholder']="Descripció"
    form.fields['preu'].widget.attrs['placeholder']="Preu"
    return render (request, 'discos/editar_disc.html', {'form': form})    


def cercador(request):
    query = request.GET.get('q', '')
    tipus= request.GET.get('tipus_de_recerca')
    if query:
       
        if tipus == "titol":
            #discos
            q_consulta = Q(titol__icontains = query )
        elif tipus == "grup":
            #discos
            q_consulta = Q(grup__icontains = query )
        elif tipus == "genere":
            q_consulta = Q(genere_icontains = query )
            
        results = Oferta_disc.objects.filter(q_consulta)
    else:
        results = []
        
<<<<<<< HEAD
    return render_to_response("discos/index.html", {
        "llista_discos": results,
        "query": query
    })
=======
def ultims(request):
    ultims=Oferta_disc.objects.all().order_by('-data_pujada')[:20]
    ctx={'ultims_discos': ultims}
    return render(request, "discos/ultims.html",ctx)
>>>>>>> 403ef305a68b39d0d8e0e6b98e0fc39aa44c2ef1
