# Generated by Django 5.1 on 2024-09-03 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phoenix', '0002_contactmessage'),
    ]

    operations = [
        migrations.AddField(
            model_name='profil',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='photos/'),
        ),
    ]
