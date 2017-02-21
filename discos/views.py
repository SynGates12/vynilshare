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
    
def afegir_modificar_disc(request,oferta_disc_id=None):
    return redirect("discos:afegir_disc")

#
#def afegir_modificar_disc(request, oferta_disc_id=None):
#    SupplyForm = modelform_factory(Suppliers, exclude=())
#    unaSupplier= Suppliers()
#    if id_supplier:
#        unaSupplier = get_object_or_404(Suppliers, pk=id_supplier)
#    if request.method == 'POST':
#        form = SupplyForm(request.POST, instance = unaSupplier)
#        if form.is_valid():
#            form.save()
#            messages.info(request, "Molt be, s'ha afegit correctament.")
#            return redirect('taulell:List_Supplier')
#    else:
#        form = SupplyForm(instance = unaSupplier)
#    for f in form.fields:
#        form.fields[f].widget.attrs['class'] = 'form-control'
#    return render(request, 'afegir_modificar_Supplier.html',
#                  {'form': form,
#                   'capcelera': "Manteniment de Caselles"} )
#



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
        
        
        