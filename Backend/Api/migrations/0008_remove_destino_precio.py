# Generated by Django 5.0.1 on 2024-01-17 23:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0007_destino_precio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='destino',
            name='precio',
        ),
    ]
