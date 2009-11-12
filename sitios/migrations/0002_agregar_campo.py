
from south.db import db
from django.db import models
from sitios.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'Autor'
        db.create_table('sitios_autor', (
            ('id', orm['sitios.autor:id']),
            ('nombre', orm['sitios.autor:nombre']),
            ('email', orm['sitios.autor:email']),
        ))
        db.send_create_signal('sitios', ['Autor'])
        
        # Adding field 'Entrada.autor_fk'
        db.add_column('sitios_entrada', 'autor_fk', orm['sitios.entrada:autor_fk'])
        
        # Adding field 'Sitio.tags'
        db.add_column('sitios_sitio', 'tags', orm['sitios.sitio:tags'])
        
    
    
    def backwards(self, orm):
        
        # Deleting model 'Autor'
        db.delete_table('sitios_autor')
        
        # Deleting field 'Entrada.autor_fk'
        db.delete_column('sitios_entrada', 'autor_fk_id')
        
        # Deleting field 'Sitio.tags'
        db.delete_column('sitios_sitio', 'tags')
        
    
    
    models = {
        'sitios.autor': {
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'sitios.entrada': {
            'autor': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'autor_fk': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sitios.Autor']"}),
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
