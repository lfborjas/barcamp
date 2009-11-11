from models import Entrada
from django.forms.models import ModelForm
from django.forms.fields import DateField
from django.contrib.admin import widgets 

class MyDateWidget(widgets.AdminDateWidget):
    class Media:
        extend=False
        js=('/my_admin/jsi18n/',
             '/media/js/core.js',
             '/media/js/calendar.js',
             '/media/js/admin/DateTimeShortcuts.js'
             )

#un form sencillo para las entradas
class EntradaForm(ModelForm):
    #personalizamos el campo de fecha para tener un calendario en vez de texto plano
    fecha_pub=DateField(widget=MyDateWidget)
    #definimos el modelo a representar:
    class Meta:
        model=Entrada
        exclude=['sitio']
    #le damos el javascript que necesita el widget
    #class Media:
    #    js= ('/my_admin/jsi18n/',
    #         '/media/js/core.js')+widgets.AdminDateWidget.Media.js
