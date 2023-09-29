from django.contrib import admin
from .models import *


@admin.register(Stand)
class StandAdmin(admin.ModelAdmin):
    list_display = ('localizacao', 'valor')
