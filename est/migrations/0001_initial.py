# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-23 19:49
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('gps', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='CentroNegocios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=128, null=True)),
                ('codigo', models.CharField(blank=True, max_length=24, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=128)),
                ('fono', models.CharField(max_length=128)),
                ('tipo_contacto', models.CharField(blank=True, max_length=128, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=128, null=True)),
                ('rut', models.CharField(blank=True, max_length=128, null=True)),
                ('contacto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='est.Contacto')),
            ],
        ),
        migrations.CreateModel(
            name='Planta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=128, null=True)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
                ('empresa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='est.Empresa')),
            ],
        ),
        migrations.CreateModel(
            name='Riesgo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=128, null=True)),
                ('tipo', models.CharField(blank=True, max_length=128, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=128, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Trabajador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=128, null=True)),
                ('rut', models.CharField(blank=True, max_length=128, null=True)),
                ('centroNegocios', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='est.CentroNegocios')),
                ('contacto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='est.Contacto')),
                ('empresa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='est.Empresa')),
                ('gps', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gps.Devices')),
                ('rol', models.ManyToManyField(to='est.Rol')),
                ('supervisor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='est.Trabajador')),
            ],
        ),
        migrations.CreateModel(
            name='Zona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=128, null=True)),
                ('uso', models.CharField(blank=True, max_length=128, null=True)),
                ('zona', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
                ('planta', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='est.Planta')),
                ('riesgo', models.ManyToManyField(blank=True, null=True, to='est.Riesgo')),
            ],
        ),
        migrations.AddField(
            model_name='rol',
            name='zonas_permitidas',
            field=models.ManyToManyField(to='est.Zona'),
        ),
        migrations.AddField(
            model_name='centronegocios',
            name='planta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='est.Planta'),
        ),
        migrations.AddField(
            model_name='centronegocios',
            name='zonas',
            field=models.ManyToManyField(to='est.Zona'),
        ),
    ]
