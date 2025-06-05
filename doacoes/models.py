from django.db import models

class RegistroDoacoes(models.Model):
    data_registro = models.DateField("Data do Registro", auto_now_add=True)
    
    # Itens contáveis
    cestas_basicas = models.PositiveIntegerField("Cestas Básicas", default=0)
    roupas = models.PositiveIntegerField("Roupas", default=0)
    familias_impactadas = models.PositiveIntegerField("Famílias Impactadas", default=0)

    # Itens com unidade de medida
    alimentos_kg = models.DecimalField("Alimentos (kg)", max_digits=10, decimal_places=2, default=0)
    alimentos_ton = models.DecimalField("Alimentos (toneladas)", max_digits=10, decimal_places=2, default=0)
    agua_mineral_litros = models.DecimalField("Água Mineral (litros)", max_digits=10, decimal_places=2, default=0)

    class Meta:
        verbose_name = "Registro de Doações"
        verbose_name_plural = "Registros de Doações"

    def __str__(self):
        return f"Registro em {self.data_registro}"
