# Generated by Django 4.2.13 on 2024-09-24 07:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phoenix', '0005_remove_avis_produit'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='panier',
            name='profil',
        ),
    ]
