# Generated by Django 5.0.4 on 2024-04-26 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0003_alter_log_usuari'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='disponibilidad',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='article',
            name='ejemplares',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='llibre',
            name='ISBN',
            field=models.CharField(max_length=20),
        ),
    ]