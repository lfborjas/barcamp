
from south.db import db
from django.db import models
from sitios.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Deleting field 'Entrada.autor'
        db.delete_column('sitios_entrada', 'autor')
        
    
    
    def backwards(self, orm):
        
        # Adding field 'Entrada.autor'
        db.add_column('sitios_entrada', 'autor', orm['sitios.entrada:autor'])
        
    
    
    models = {
        'sitios.autor': {
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'sitios.entrada': {
            'autor_fk': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sitios.Autor']", 'null': 'True'}),
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
            'tags': ('django.db.models.fields.CharField', [], {'default': "'barcamp'", 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'tipo': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }
    
    complete_apps = ['sitios']
