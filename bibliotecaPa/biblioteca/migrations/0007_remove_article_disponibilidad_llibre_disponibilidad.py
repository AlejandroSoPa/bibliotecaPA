# Generated by Django 5.0.4 on 2024-04-29 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0006_remove_llibre_disponibilidad_article_disponibilidad'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='disponibilidad',
        ),
        migrations.AddField(
            model_name='llibre',
            name='disponibilidad',
            field=models.BooleanField(default=True),
        ),
    ]
