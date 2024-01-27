# Generated by Django 5.0.1 on 2024-01-18 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0011_alter_user_destino'),
    ]

    operations = [
        migrations.RenameField(
            model_name='destino',
            old_name='precio',
            new_name='precio_original',
        ),
        migrations.AddField(
            model_name='destino',
            name='precio_con_descuento',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]