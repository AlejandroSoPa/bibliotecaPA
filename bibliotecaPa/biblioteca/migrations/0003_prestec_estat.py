# Generated by Django 5.0.4 on 2024-05-06 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0002_alter_usuari_telefon'),
    ]

    operations = [
        migrations.AddField(
            model_name='prestec',
            name='estat',
            field=models.BooleanField(default=False),
        ),
    ]