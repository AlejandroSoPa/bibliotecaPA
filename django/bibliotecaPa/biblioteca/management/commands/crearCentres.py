from django.core.management.base import BaseCommand
from faker import Faker
from biblioteca.models import Centre

fake = Faker()

class Command(BaseCommand):
    help = 'Crea Centres'

    def handle(self, *args, **kwargs):
        bibliotecas = [
            "Biblioteca Mari Carmen",
            "Biblioteca Central de Cornella",
            "Biblioteca Sant Ildefons",
            # Agrega más nombres de bibliotecas aquí...
        ]

        for nombre in bibliotecas:
            Centre.objects.create(nom=nombre)

        self.stdout.write(self.style.SUCCESS('Centres creats correctament'))
