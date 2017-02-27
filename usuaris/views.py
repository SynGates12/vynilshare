# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from .forms import LoginForm, nou_usuari_form
from django.core.urlresolvers import reverse
from django.forms import modelform_factory
from .models import Perfil, Missatge
from discos.models import Oferta_disc
from django.db.models import Q
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth import ( login as authLogin,
                                  authenticate,
                                  logout as authLogout )
from django.contrib import messages

#CREAR USUARI -------
def crear_usuari(request, perfil_id=None):
    
    if request.method == 'POST':
        form = nou_usuari_form(request.POST )
        
        if form.is_valid():
            email = form.cleaned_data['email']
            repetit = User.objects.filter( username = email )
            #mirem si està repetit i llencem missatge error "cuidadín"
            if repetit:
                messages.error( request, "Aquest nom d'usuari ja existeix a la base de dades")
            else:
                password = form.cleaned_data['password']
                #creem el nou usuari
                nou_usuari = User.objects.create_user( username = email, email = email, password = password )
                
                messages.info(request,"Usuari creat correctament")
                return redirect('discos:index')
    else:
        form = nou_usuari_form()
    
    for f in form.fields:
       form.fields[f].widget.attrs['class'] = 'formulari inputForm'
       
    form.fields['email'].widget.attrs['placeholder']="Email"
    form.fields['password'].widget.attrs['placeholder']="Contrasenya"
    form.fields['email'].widget.attrs['required']="required"
    form.fields['password'].widget.attrs['required']="required"
    
    return render(request, 'crear_usuari.html', {'form': form,} )

#MODIFICAR PERFIL UN COP CREAT: formulari UserDjango + formulari Perfil ---
def modificar_perfil(request):
    usuariForm = modelform_factory(User,fields=("first_name","last_name"))
    profileForm = modelform_factory(Perfil,fields=("CP", "localitat"))
    unPerfil = request.user.perfil
    unUsuari = request.user
    
    if request.method == 'POST':
        formUsuari = usuariForm(request.POST, instance = unUsuari)
        formPerfil = profileForm(request.POST, request.FILES, instance = unPerfil)
        formUsuariValid = formUsuari.is_valid()
        formPerfilValid = formPerfil.is_valid()
            
        if formUsuariValid and formPerfilValid:
            formUsuari.save()
            formPerfil.save()
            messages.info(request,"S'han modificat les dades correctament")
            return redirect('discos:index')
    else:
        formUsuari = usuariForm(instance = unUsuari)
        formPerfil = profileForm(instance = unPerfil)
        
    for f in formUsuari.fields:
       formUsuari.fields[f].widget.attrs['class'] = 'formulari'
    for f in formPerfil.fields:
       formPerfil.fields[f].widget.attrs['class'] = 'formulari'
   
    formUsuari.fields['first_name'].widget.attrs['placeholder']="Nom"
    formUsuari.fields['last_name'].widget.attrs['placeholder']="Cognoms"
    formPerfil.fields['CP'].widget.attrs['placeholder']="Codi postal"
    formPerfil.fields['localitat'].widget.attrs['placeholder']="Localitat"
    
    return render(request, 'modificar_perfil.html', {'formPerfil': formPerfil, 
                                                     'formUsuari': formUsuari } )

#MENÚ USUARI -----------
def menu_usuari(request):
    discos_oferta= request.user.perfil.discos_oferta.all()
#    venuts = request.user.perfil.discos_oferta.filter(venut=True)
    ctx={"discos_meus":discos_oferta}        
    return render(request,"menu_usuari.html",ctx)


  

#LOGEJAR-SE ------
def login(request):

    #si tot es POST:
    if request.method=='POST':
        form=LoginForm( request.POST )

        if form.is_valid():
            user=authenticate( username = form.cleaned_data['username'],
                               password = form.cleaned_data['password'])
               
            if user and user.is_active:
                #si tot és ok:
                authLogin( request, user )
                next = request.GET.get('next')
                messages.info(request,"Benvingut")
                return redirect(next or 'discos:index')

            else:
                messages.error(request,"Usuari o password incorrecte o usuari no actiu")
                print "error"
           
    else:
        form=LoginForm()
   
    ctx={ 'form':form, }
    form.fields['username'].widget.attrs['placeholder']="Email"
    form.fields['password'].widget.attrs['placeholder']="Contrasenya"
    form.fields['username'].widget.attrs['required']="required"
    form.fields['password'].widget.attrs['required']="required"
    
    return render(request, 'login.html', ctx )

#DESLOGUEJAR-SE: me voy! ---    
def logout(request):
    authLogout( request )
    return redirect( 'discos:index')