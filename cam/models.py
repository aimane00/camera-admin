from django.conf import settings
from django.db import models
from django.utils import timezone


class Site(models.Model):
    nom = models.CharField(max_length=300)

    def __str__(self):
        return self.nom



class Camera(models.Model):
    nom = models.CharField(max_length=300)
    reference = models.CharField(max_length=300)
    emplacement = models.CharField(max_length=300)
    date_installaion= models.DateTimeField(blank=True, null=True)
    site = models.ForeignKey(Site, related_name='Site', null=True, on_delete=models.CASCADE)
    frais = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    def __str__(self):
        return '%s %s' % (self.nom, self.reference)



class Reparation(models.Model):
    date_reparation = models.DateTimeField(blank=True, null=True)
    frais = models.DecimalField(max_digits=10, decimal_places=2)
    descriptif = models.TextField() 
    camera = models.ForeignKey(Camera, related_name='Camera', null=True, on_delete=models.CASCADE)
    


