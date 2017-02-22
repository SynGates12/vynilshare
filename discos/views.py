# -*- coding: utf-8 -*-
from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from discos.models import Oferta_disc
from django.forms import modelform_factory
from django.db.models import Q
from .forms import SearchForm, ContacteForm
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
    

def contacte(request):
    
    if request.method =="POST":
        form=ContacteForm(request.POST)
        if form.is_valid():
            nom= form.cleaned_data['nom']
            email = form.cleaned_date['email']
            missatge=form.cleaned_data['missatge']
        return redirect ('discos:index')
            
    else:
        form = ContacteForm()
    
    for f in form.fields:
       form.fields[f].widget.attrs['class'] = 'formulari'
   
    return render (request, 'discos/contacte.html', {'form': form})

    
    
def afegir_disc(request,oferta_disc_id=None):
    DiscForm = modelform_factory(Oferta_disc, fields=('titol', 'grup','anny','genere'))
    unOferta = Oferta_disc()
    
    if request.method == 'POST':
        form = DiscForm (request.POST,request.FILES, instance= unOferta)
        if form.is_valid():
           form.save()
           messages.info(request,"pujat correctament disc")
           return redirect("discos:llista")    
    else:
        form= DiscForm (instance = unOferta)
    for f in form.fields:
        form.fields[f].widget.attrs['class'] = 'form-group'
        
        form.fields['genere'].widget.attrs['placeholder']="Email"
 
    return render (request, 'discos/afegir_disc.html', {'form': form})    

def cercador (request):
    #si és un POST
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            tipus= form.cleaned_data['tipus_de_recerca']
            text = form.cleaned_date['text']
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
        
        
        