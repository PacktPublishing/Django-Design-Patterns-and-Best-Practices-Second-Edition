from django.contrib import admin
from . import models


class SightingAdmin(admin.ModelAdmin):
    list_display = ('superhero', 'power', 'location', 'sighted_on')
    date_hierarchy = 'sighted_on'
    search_fields = ['superhero']
    ordering = ['superhero']


admin.site.register(models.Origin)
admin.site.register(models.Location)
admin.site.register(models.Sighting, SightingAdmin)
