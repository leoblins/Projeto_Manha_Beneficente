from django.contrib import admin
from .models import RegistroDoacoes

@admin.register(RegistroDoacoes)
class RegistroDoacoesAdmin(admin.ModelAdmin):
    fields = (
        'cestas_basicas',
        'roupas',
        'agua_mineral_litros',
        'familias_impactadas',
    )
