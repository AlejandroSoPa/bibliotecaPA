from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.auth import get_user_model
from biblioteca.models import Usuari, Centre
from faker import Faker
from random import choice
from datetime import datetime
import os

User = get_user_model()

class Command(BaseCommand):
    help = 'Seed the database with dummy data for Usuari model'

    def handle(self, *args, **kwargs):
        # Crear algunos grupos de ejemplo si no existen

        default_group_bibli, _ = Group.objects.get_or_create(name='MiGrupo')

        permissions = Permission.objects.all()
        default_group_bibli.permissions.set(permissions)

        if not Group.objects.exists():
            self.stdout.write(self.style.ERROR('No existen grupos en la base de datos.'))
            return
        else:
            self.stdout.write(self.style.SUCCESS('Grupos encontrados en la base de datos.'))  

        fake = Faker('es_ES')
        centres = Centre.objects.all()     

        # Crear algunos usuarios de ejemplo
        for i in range(3):
            # Crear un usuario de ejemplo con datos aleatorios
            username = fake.user_name()
            admin = True
            email = fake.email()
            first_name = fake.first_name()
            last_name = fake.last_name()
            password = "IETI202$"
            phone = fake.phone_number()[:9]  # Limitar el número de teléfono a 9 caracteres
            data_naixement = fake.date_of_birth(minimum_age=16, maximum_age=40)
            centre = choice(centres)

            # Crear el usuario con los datos generados
            user = Usuari.objects.create_user(
                username=username,
                email=email,
                first_name=first_name,
                last_name=last_name,
                password=password,
                admin=admin,
                telefon=phone,
                data_naixement=data_naixement,
                centre=centre
            )

            # Asignar el usuario al grupo por defecto
            user.groups.add(default_group_bibli)

        
        default_group, _ = Group.objects.get_or_create(name='default')
        
        for i in range(97):
            # Crear un usuario de ejemplo con datos aleatorios
            username = fake.user_name()
            admin = fake.boolean(False)
            email = fake.email()
            first_name = fake.first_name()
            last_name = fake.last_name()
            password = "IETI202$"
            phone = fake.phone_number()[:9]  # Limitar el número de teléfono a 9 caracteres
            data_naixement = fake.date_of_birth(minimum_age=18, maximum_age=80)
            centre = choice(centres)

            # Crear el usuario con los datos generados
            user = Usuari.objects.create_user(
                username=username,
                email=email,
                first_name=first_name,
                last_name=last_name,
                password=password,
                admin=admin,
                telefon=phone,
                data_naixement=data_naixement,
                centre=centre
            )

            # Asignar el usuario al grupo por defecto
            user.groups.add(default_group)

        self.stdout.write(self.style.SUCCESS('Data seeded successfully'))

    def get_random_image_path(self):
        # Directorio donde se encuentran las imágenes de ejemplo
        image_dir = 'path/to/your/image/directory'

        # Obtener una lista de las imágenes disponibles
        # image_files = [f for f in os.listdir(image_dir) if os.path.isfile(os.path.join(image_dir, f))]

        # Seleccionar una imagen al azar de la lista
        #if image_files:
            #return os.path.join(image_dir, random.choice(image_files))
        #else:
        return 'fotos_perfil/default.jpg'  # Si no hay imágenes disponibles, se usa una por defecto
