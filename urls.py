from django.conf.urls.defaults import *
from django.conf import settings
from django.views.generic.simple import direct_to_template
from django.views.generic.list_detail import  object_list
from django.views.generic.create_update import create_object
from sitios.models import Sitio
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

webcomics_info={
	'queryset': Sitio.objects.filter(tipo='WC'),
	'extra_context': {'objeto': 'webcomics'}
}

blogs_info={
	'queryset': Sitio.objects.filter(tipo='B') ,
	'extra_context': {'objeto': 'blogs'}
}


urlpatterns = patterns('',
    # Example:
     (r'^$', direct_to_template, {'template': 'base.html'}),
     (r'^webcomics/$', object_list,webcomics_info),
     (r'^blogs/$', object_list, blogs_info),
     (r'^webcomics/nuevo/$', create_object, {'model': Sitio, 'post_save_redirect': '/webcomics/'}),	
     (r'^blogs/nuevo/$', create_object, {'model': Sitio, 'post_save_redirect': '/blogs/'}),
     #uso de una wrapper para una generic view:
     #(r'^webcomics/(?P<id>\d+)/entradas/', 'sitios.views.ver_entradas', {'tipo': 'WC'}),     
     (r'^(?P<tipo>\w+)/(?P<id_sitio>\d+)/entradas/$', 'sitios.views.ver_entradas'),
     #una view normal:
     #(r'^webcomics/(?P<id>\d+)/entradas/nueva/', 'sitios.views.agregar_entradas'),
     (r'^(?P<tipo>\w+)/(?P<id_sitio>\d+)/entradas/nueva/$', 'sitios.views.agregar_entrada'),
	
	
     

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     (r'^admin/', include(admin.site.urls)),
    #Para tener disponibles las traducciones de javascript de admin:
     (r'^my_admin/jsi18n', 'django.views.i18n.javascript_catalog'),

)

if settings.DEBUG:
        urlpatterns += patterns('',
                (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_DOC_ROOT}),
        )

