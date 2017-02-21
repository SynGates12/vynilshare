# -*- coding: utf-8 -*-
from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from discos.models import Oferta_disc
from django.db.models import Q
from .forms import SearchForm
# Create your views here.

def index(request):
    discos= Oferta_disc.objects.all();
    ctx={'llista_discos': discos}
    return render(request, "discos/index.html",ctx)
    

def vinil_informacio(request,id_Oferta_disc):
    vinil = get_object_or_404(Oferta_disc,pk=id_Oferta_disc)
    ctx={'vinil': vinil}
    return render(request,"discos/vinil_informacio.html",ctx)
    

def contacte(request):
    return redirect("discos:contacte")
    

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
        
        
        