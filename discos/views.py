# -*- coding: utf-8 -*-
from django.shortcuts import render,get_object_or_404,redirect, render_to_response
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from discos.models import Oferta_disc
from usuaris.models import Perfil, Missatge
from django.contrib.auth.models import User
from django.forms import modelform_factory
from django.db.models import Q
from .forms import SearchForm, ContacteForm
from .forms import DiscForm
from django.contrib import messages
 
# Create your views here.

#INDEX------------
def index(request):
    discos= Oferta_disc.objects.all();
    ctx={'llista_discos': discos}
    return render(request, "discos/index.html",ctx)

#RECOMANATS -----------    
def recomanats(request):
    recomendados=Oferta_disc.objects.all().order_by('?')[:12]
    ctx={'recomana_discos': recomendados}
    
    return render(request, "discos/recomanats.html",ctx)

#ULTIMS -----------    
def ultims(request):
    llista_ultims=Oferta_disc.objects.all().order_by("data_pujada")
    ctx={'llista_ultims': llista_ultims}
    return render (request, "discos/ultims.html",ctx)



#VINIL INFORMACIÓ -------    
def vinil_informacio(request,oferta_disc_id):
    disc = get_object_or_404(Oferta_disc,pk=oferta_disc_id)
    ctx={'disc': disc}
    return render(request,"discos/vinil_informacio.html",ctx)


#DISCOS VENUTS --------    
def discos_venuts(request):

    venuts= request.user.perfil.discos_oferta.filter(venut=True)
    ctx={'venuts': venuts}
    return render (request, "discos/discos_venuts.html", ctx)


#INFORMACIO USUARI ------
def usuari_informacio(request,usuari_id):
    usuari=Oferta_disc.objects.get(usuari_venedor_id=usuari_id)
    discos_oferta= usuari.discos_oferta.all()
    valoracio=usuari.valoracio
    
    return render (request, "discos/usuari_informacio.html", { "discos_oferta":discos_oferta , "valoracio":valoracio })  


#CONTACTE -----------
def contacte(request):
    #si métode és POST
    if request.method =="POST":
        form=ContacteForm(request.POST)
        if form.is_valid():
            nom= form.cleaned_data['nom']
            email = form.cleaned_data['email']
            missatge=form.cleaned_data['missatge']
            form.save()
        return redirect ('discos:index')
            
    else: #que aparegui de nou el formulari
        form = ContacteForm()
    #widgets del formulari
    for f in form.fields:
       form.fields[f].widget.attrs['class'] = 'formulari'
   
    form.fields['nom'].widget.attrs['placeholder']="Nom"
    form.fields['email'].widget.attrs['placeholder']="Email"
    form.fields['missatge'].widget.attrs['placeholder']="Missatge"
    form.fields['nom'].widget.attrs['required']="required"
    form.fields['email'].widget.attrs['required']="required"
    form.fields['missatge'].widget.attrs['required']="required"
    
    return render (request, 'discos/contacte.html', {'form': form})

#AFEGIR DISC --------
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
           
           #creem l'objecte OFERTA_DISC amb les dades rebudes
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
        
    return render (request, 'discos/afegir_disc.html', {'form': form} )    

   
#EDITAR DISC EXISTENT
def editar_disc(request, oferta_disc_id):
    EditForm = modelform_factory(Oferta_disc, fields=('titol', 'grup','anny','genere','estat','descripcio','preu', 'image'))
    unEdit = Oferta_disc()
    
    #comprovem que existeix l'oferta_disc
    if oferta_disc_id:
        unEdit = get_object_or_404(Oferta_disc, pk=oferta_disc_id)
        
    if request.method == 'POST':
        form = EditForm (request.POST,request.FILES, instance= unEdit)
        if form.is_valid():
           form.save()
           messages.info(request,"disc canviat correctament")
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
    
    return render (request, 'discos/editar_disc.html', {'form': form} )    

#ESBORRAR DISC -----
def eliminar_disc(request,oferta_disc_id):
    disc = Oferta_disc.objects.get(id=oferta_disc_id)
    
    #si el métode és POST
    if request.method == 'POST':
        disc.delete()
        return redirect('usuaris:menu_usuari')

    else:
        return render(request, 'discos/eliminar_disc.html', {'disc': disc})




#CERCADOR que tantas làgrimas ha costao ----
def cercador(request):
    #fem la consulta
    query = request.GET.get('q', '')
    tipus= request.GET.get('tipus_de_recerca')
    
    if query:
        if tipus == "titol":
            #discos
            q_consulta = Q(titol__icontains = query )
        elif tipus == "grup":
            #grup
            q_consulta = Q(grup__icontains = query )
        elif tipus == "genere":
            #genere
            q_consulta = Q(genere_icontains = query )
        #resultats me'ls fiques a la variable 'results'    
        results = Oferta_disc.objects.filter(q_consulta)
    else:
        results = [] #que no aparegui res
        
    return render( request, "discos/index.html", 
                                { "llista_discos": results,
                                   "query": query }
                               )

