

from django.contrib import admin
from .models import *


@admin.register(PoEDivinationCard)
class PoEDivinationCardAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'description', 'image', 'stack_size', 'slug'
    )
