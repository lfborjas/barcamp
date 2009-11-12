from django.db import models
#from django.utils.translation import ugettext as _
# Create your models here.
SITE_CHOICES=(
	('WC', 'webcomic'),
	('B', 'blog'),
)

class Sitio(models.Model):
	nombre=models.CharField(max_length=200)
	direccion=models.URLField()
	tipo=models.CharField(max_length=200, choices=SITE_CHOICES)
	tags=models.CharField(max_length=200, blank=True, null=True, default="barcamp")	
	#tags=somekindofset
	def __unicode__(self):
		return self.nombre

#Y si queremos restringirlo?
#	class Meta:
#		unique_together=("nombre", "direccion")

class Autor(models.Model):
	nombre=models.CharField(max_length=200)
	email=models.EmailField(blank=True)
	def __unicode__(self):
		 return self.nombre

class Entrada(models.Model):
	sitio=models.ForeignKey(Sitio)
	titulo=models.CharField(max_length=200, blank=True)
	#Y si nos importase tener autores?
	#autor_viejo=models.CharField(max_length=200, blank=True)
	#le ponemos un nombre temporal:
	autor=models.ForeignKey(Autor)
	direccion=models.URLField()
	#y si la fecha de salida importa?
	fecha_pub=models.DateField(auto_now_add=True)
	
	def __unicode__(self):
		return self.direccion


	
