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
	'queryset': Sitio.objects.filter(tipo='WC')
}

blogs_info={
	'queryset': Sitio.objects.filter(tipo='B') 
}


urlpatterns = patterns('',
    # Example:
     (r'^$', 'direct_to_template', {'template': 'base.html'})
     (r'^webcomics/$', 'object_list',webcomics_info),
     (r'^blogs/$', 'object_list', blogs_info),
     (r'^webcomics/nuevo/$', 'create_object', {'model': Sitio, 'post_save_redirect': '/webcomics/'})	
     (r'^blogs/nuevo/$', 'create_object', {'model': Sitio, 'post_save_redirect': '/blogs/'})	
	
	
     

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     (r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
        urlpatterns += patterns('',
                (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_DOC_ROOT}),
        )

