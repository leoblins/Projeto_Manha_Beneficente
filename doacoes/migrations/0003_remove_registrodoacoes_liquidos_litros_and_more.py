# Generated by Django 5.2.2 on 2025-06-05 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doacoes', '0002_remove_registrodoacoes_agua_mineral_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registrodoacoes',
            name='liquidos_litros',
        ),
        migrations.AddField(
            model_name='registrodoacoes',
            name='agua_mineral_litros',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Água Mineral (litros)'),
        ),
    ]
