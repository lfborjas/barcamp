# Create your views here.
import models
from forms import EntradaForm
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.list_detail import  object_list
#los tipos de sitios permitidos:
TIPOS_DE_SITIOS=['webcomics', 'blogs']

def ver_entradas(request, tipo, id_sitio):
    """
        Mostraremos las entradas para un sitio en particular.
        El tipo debe pertenecer a los TIPOS_DE_SITIOS.
        el id_sitio es el id del sitio en la base de datos. 
        Si el tipo sitio no existe, redirigir a la principal.
        Si el sitio no existe, redirigir a la lista.
    """
    if not tipo in TIPOS_DE_SITIOS:
        return HttpResponseRedirect('/')
    #notemos que no es necesario buscar por tipo...
    try:
         sitio=models.Sitio.objects.get(pk=id_sitio)
    except models.Sitio.DoesNotExist:
        return HttpResponseRedirect('/%s/'%tipo)
    
    entradas=models.Entrada.objects.filter(sitio=sitio)
    return object_list(request,
                       queryset=entradas,
                       extra_context= 
                            {'agregar_a': '/%s/%s/entradas/nueva/'%(tipo, id_sitio),
                             'nombre_sitio': sitio.nombre}
                         )

def agregar_entrada(request, tipo, id_sitio):
    """
        Igual que antes, vemos si todo existe bien antes de proceder. Luego procesamos
        el form si viene algo en el post o lo mostramos por primera vez.
    """    
    if not tipo in TIPOS_DE_SITIOS:
        return HttpResponseRedirect('/')
    #notemos que no es necesario buscar por tipo...
    try:
         sitio=models.Sitio.objects.get(pk=id_sitio)
    except models.Sitio.DoesNotExist:
        return HttpResponseRedirect('/%s/'%tipo)
    
    if request.method=='POST':
        form=EntradaForm(request.POST)
        if form.is_valid():
            data=form.save(commit=False)
            data.sitio_id=id_sitio
            data.save()
            return HttpResponseRedirect('/%s/%s/entradas/'%(tipo, id_sitio))
        else:
            return render_to_response('sitios/entrada_form.html',{'form': form, 'nombre_sitio': sitio.nombre} )
    else:
        #es un form nuevo:
        form=EntradaForm()
        return render_to_response('sitios/entrada_form.html',{'form': form, 'nombre_sitio': sitio.nombre} )