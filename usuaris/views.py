# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404, redirect
from .forms import LoginForm
from django.forms import modelform_factory
from .models import Perfil
from django.http import HttpResponseRedirect
from django.contrib.auth import ( login as authLogin,
                                  authenticate,
                                  logout as authLogout )
from django.contrib import messages


# Create your views here.




def Crear_usuari(request, perfil_id=None):
    UsuariForm = modelform_factory(Perfil, fields=("username","password","email","firstname","lastname","localitat","CP"))
    unUsuari = Perfil()
    if perfil_id:
        unUsuari = get_object_or_404(Perfil, pk=perfil_id)
    if request.method == 'POST':
        form = UsuariForm(request.POST, instance = unUsuari)
        if form.is_valid():
            form.save()
            return redirect('menu.usuari',perfil_id)
    else:
        form = UsuariForm(instance = unUsuari)
    for f in form.fields:
        form.fields[f].widget.attrs['class'] = 'form-control'
    return render(request, 'form.html',
                  {'form': form,} )   
    
    
    

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
                return redirect(next or 'discos:index'  )

            else:
                messages.error(request,"Usuari o password incorrecte o usuari no actiu")
    else:
        #si es un GET:
        form=LoginForm()
        ctx={ 'form':form, }
        for f in form.fields:
            form.fields[f].widget.attrs['class'] = 'form-control'
        return render(request, 'form.html', ctx )

def logout(request):
    authLogout( request )
    return redirect( 'discos:index' )