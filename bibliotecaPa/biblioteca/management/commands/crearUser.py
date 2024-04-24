from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from biblioteca.models import Usuari, Centre
from faker import Faker
from random import choice
from datetime import datetime

class Command(BaseCommand):
    help = 'Seed the database with dummy data for Usuari model'

    def handle(self, *args, **kwargs):
        # Crear algunas instancias de usuarios de ejemplo
        fake = Faker()
        centres = Centre.objects.all()

        if not centres.exists():
            self.stdout.write(self.style.ERROR('No existen centros en la base de datos.'))
            return

        for _ in range(5):
            # Generar datos aleatorios para el usuario
            username = fake.user_name()
            email = fake.email()
            first_name = fake.first_name()
            last_name = fake.last_name()
            password = Usuari.objects.make_random_password()
            data_naixement = fake.date_of_birth(minimum_age=18, maximum_age=80)
            centre = choice(centres)

            # Crear el usuario con los datos generados
            user = Usuari.objects.create_user(
                username=username,
                email=email,
                first_name=first_name,
                last_name=last_name,
                password=password,
                data_naixement=data_naixement,
                centre=centre
            )

            self.stdout.write(self.style.SUCCESS(f'Usuari creado: {user.username}'))

        self.stdout.write(self.style.SUCCESS('Data seeded successfully for Usuari model'))
