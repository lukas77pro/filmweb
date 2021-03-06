# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-01 00:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=100)),
                ('nazwa_oryginalna', models.CharField(max_length=100)),
                ('czas_trwania', models.PositiveIntegerField(null=True)),
                ('rok_produkcji', models.PositiveIntegerField(null=True)),
                ('data_premiery', models.DateField(null=True)),
                ('data_premiery_polska', models.DateField(null=True)),
                ('budzet', models.PositiveIntegerField(null=True)),
                ('opis', models.TextField(blank=True)),
                ('ocena', models.FloatField(default=0.0)),
                ('ilosc_ocen', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Gatunek',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Kategoria_nagrody',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kategoria', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Kraj',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Nagroda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=50)),
                ('opis', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Nagroda_rozdana',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_wydania', models.DateField(null=True)),
                ('film', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Film')),
                ('kategoria', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Kategoria_nagrody')),
                ('nagroda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Nagroda')),
            ],
        ),
        migrations.CreateModel(
            name='Osoba',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imie', models.CharField(max_length=50)),
                ('nazwisko', models.CharField(max_length=50)),
                ('data_urodzenia', models.DateField(blank=True, null=True)),
                ('data_smierci', models.DateField(blank=True, null=True)),
                ('biografia', models.TextField(blank=True)),
                ('wzrost', models.IntegerField(blank=True, null=True)),
                ('ocena', models.FloatField(default=0.0)),
                ('ilosc_ocen', models.PositiveIntegerField(default=0)),
                ('kraj_urodzenia', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Kraj')),
            ],
        ),
        migrations.CreateModel(
            name='Recenzja',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('film', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Film')),
                ('osoba', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Osoba')),
            ],
        ),
        migrations.CreateModel(
            name='Rola',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ocena', models.FloatField(default=0.0)),
                ('ilosc_ocen', models.PositiveIntegerField(default=0)),
                ('film', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Film')),
                ('osoba', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Osoba')),
            ],
        ),
        migrations.CreateModel(
            name='Zawod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='rola',
            name='zawod',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Zawod'),
        ),
        migrations.AddField(
            model_name='nagroda_rozdana',
            name='osoba',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Osoba'),
        ),
        migrations.AddField(
            model_name='kategoria_nagrody',
            name='nagroda',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Nagroda'),
        ),
        migrations.AddField(
            model_name='film',
            name='gatunki',
            field=models.ManyToManyField(to='api.Gatunek'),
        ),
        migrations.AddField(
            model_name='film',
            name='produkcja',
            field=models.ManyToManyField(to='api.Kraj'),
        ),
    ]
