# Generated by Django 5.0.1 on 2024-01-17 23:14

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Destino',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pais', models.CharField(max_length=10)),
                ('ciudad', models.CharField(max_length=10)),
                ('rating', models.IntegerField(default=5)),
                ('descuento', models.BooleanField(default=False)),
                ('description', models.TextField(blank=True)),
                ('fecha_publicacion', models.DateTimeField(default=datetime.date.today)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('destino', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.SET_DEFAULT, to='Api.destino')),
            ],
        ),
    ]
