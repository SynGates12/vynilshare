# -*- coding: utf-8 -*-
from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from discos.models import Oferta_disc
from django.forms import modelform_factory
from django.db.models import Q
from .forms import SearchForm, ContacteForm, DiscForm
from django.contrib import messages
# Create your views here.

def index(request):
    discos= Oferta_disc.objects.all();
    ctx={'llista_discos': discos}
    return render(request, "discos/index.html",ctx)
    

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

    
    
def afegir_disc(request,oferta_disc_id=None):
   
    if request.method == 'POST':
        form = DiscForm(request.POST,request.FILES)
        if form.is_valid():
           titol= form.cleaned_data['titol']
           grup = form.cleaned_data['grup']
           anny=form.cleaned_data['anny']
           genere=form.cleaned_data['genere']
           anny=form.cleaned_data['preu']
           estat=form.cleaned_data['estat']
           descripcio=form.cleaned_data['descripcio']
           form.save()
           messages.info(request,"pujat correctament disc")
           return redirect("menu_usuari")    
    else:
        form= DiscForm ()
   
    for f in form.fields:
        form.fields[f].widget.attrs['class'] = 'form-control'
        form.fields['titol'].widget.attrs['placeholder']="Titol"
        form.fields['grup'].widget.attrs['placeholder']="Grup"
        form.fields['anny'].widget.attrs['placeholder']="Any"
        form.fields['preu'].widget.attrs['placeholder']="Preu"
    return render (request, 'discos/afegir_disc.html', {'form': form})    

def editar_disc(request,oferta_disc_id=None):
    EditForm = modelform_factory(Oferta_disc, fields=('titol', 'grup','anny','genere','estat','descripcio','preu'))
    unEdit = Oferta_disc()
    
    if request.method == 'POST':
        form = EditForm (request.POST,request.FILES, instance= unEdit)
        if form.is_valid():
           form.save()
           messages.info(request,"canviat correctament disc")
           return redirect("menu_usuari")    
    else:
        form= EditForm (instance = unEdit)
    for f in form.fields:
        form.fields[f].widget.attrs['class'] = 'form-group'
 
    return render (request, 'discos/editar_disc.html', {'form': form})    
    
def cercador (request):
    #si és un POST
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            tipus= form.cleaned_data['tipus_de_recerca']
            text = form.cleaned_data['text']
            if tipus == "TITOL":
                #discos
                q_consulta = Q( titol__icontains = text )
            elif tipus == "GRUP":
                #discos
                q_consulta = Q( grup__icontains = text )
            elif tipus == "GENERE":
                q_consulta = Q( genere_icontains = text )
                
        discos = Oferta_disc.objects.filter( q_consulta )   
    #si no és POST        
    else:
        #torna al formulari
        form = SearchForm()
      
    ctx={"discos":discos}    
    return render(request,"discos/cercador.html",ctx)
        
        
        