from django.contrib import admin

from .models import Familia

class FamiliaAdmin(admin.ModelAdmin):
    list_display = ('parentezco', 'nombre', 'apellido', 'edad')

admin.site.register(Familia, FamiliaAdmin)