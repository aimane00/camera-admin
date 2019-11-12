from django.contrib import admin
from .models import Camera, Site, Reparation


class CameraAdmin(admin.ModelAdmin):
    list_display = ('nom', 'reference', 'emplacement', 'date_installaion',)
    ordering = ('nom',)
    search_fields = ('nom', 'reference')


class ReparationAdmin(admin.ModelAdmin):
    list_display = ('camera', 'date_reparation', 'frais', 'descriptif',)
    ordering = ('camera',)
    search_fields = ('camera',)



class SiteAdmin(admin.ModelAdmin):
    list_display = ('nom',)
    ordering = ('nom',)
    search_fields = ('nom',)



admin.site.register(Camera, CameraAdmin)
admin.site.register(Site, SiteAdmin)
admin.site.register(Reparation, ReparationAdmin)
