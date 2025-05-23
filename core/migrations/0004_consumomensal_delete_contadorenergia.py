# Generated by Django 5.2.1 on 2025-05-20 00:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_contadorenergia'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConsumoMensal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ano', models.PositiveIntegerField()),
                ('mes', models.PositiveIntegerField()),
                ('tarifa_social', models.BooleanField(default=False)),
                ('leitura_inicial', models.DecimalField(decimal_places=2, max_digits=10)),
                ('leitura_final', models.DecimalField(decimal_places=2, max_digits=10)),
                ('consumo_kwh', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('total_pagar', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('atualizado_em', models.DateTimeField(auto_now=True)),
                ('bandeira', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.bandeira')),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.estado')),
            ],
            options={
                'ordering': ['-ano', '-mes'],
                'unique_together': {('ano', 'mes', 'estado', 'bandeira')},
            },
        ),
        migrations.DeleteModel(
            name='ContadorEnergia',
        ),
    ]
