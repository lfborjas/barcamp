
from south.db import db
from django.db import models
from sitios.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'Sitio'
        db.create_table('sitios_sitio', (
            ('id', orm['sitios.Sitio:id']),
            ('nombre', orm['sitios.Sitio:nombre']),
            ('direccion', orm['sitios.Sitio:direccion']),
            ('tipo', orm['sitios.Sitio:tipo']),
        ))
        db.send_create_signal('sitios', ['Sitio'])
        
        # Adding model 'Entrada'
        db.create_table('sitios_entrada', (
            ('id', orm['sitios.Entrada:id']),
            ('sitio', orm['sitios.Entrada:sitio']),
            ('titulo', orm['sitios.Entrada:titulo']),
            ('autor', orm['sitios.Entrada:autor']),
            ('direccion', orm['sitios.Entrada:direccion']),
            ('fecha_pub', orm['sitios.Entrada:fecha_pub']),
        ))
        db.send_create_signal('sitios', ['Entrada'])
        
    
    
    def backwards(self, orm):
        
        # Deleting model 'Sitio'
        db.delete_table('sitios_sitio')
        
        # Deleting model 'Entrada'
        db.delete_table('sitios_entrada')
        
    
    
    models = {
        'sitios.entrada': {
            'autor': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'direccion': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'fecha_pub': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sitio': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sitios.Sitio']"}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'})
        },
        'sitios.sitio': {
            'direccion': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'tipo': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }
    
    complete_apps = ['sitios']
