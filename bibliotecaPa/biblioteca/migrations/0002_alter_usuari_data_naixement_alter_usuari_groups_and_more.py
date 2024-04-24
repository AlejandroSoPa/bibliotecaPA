# Generated by Django 5.0.4 on 2024-04-23 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('biblioteca', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuari',
            name='data_naixement',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='usuari',
            name='groups',
            field=models.ManyToManyField(null=True, related_name='usuari_group', to='auth.group'),
        ),
        migrations.AlterField(
            model_name='usuari',
            name='imatge',
            field=models.ImageField(default='default.jpg', null=True, upload_to='fotos_perfil'),
        ),
        migrations.AlterField(
            model_name='usuari',
            name='user_permissions',
            field=models.ManyToManyField(null=True, related_name='usuarios_permision', to='auth.permission'),
        ),
    ]