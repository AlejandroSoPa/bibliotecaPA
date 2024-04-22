from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from biblioteca.models import Reserva, Usuari, Article
from datetime import datetime

class Command(BaseCommand):
    help = 'Seed the database with dummy data for Reserva model'

    def handle(self, *args, **kwargs):
        # Obtener algunos usuarios y artículos existentes para asignar a las reservas
        usuarios = Usuari.objects.all()
        articulos = Article.objects.all()

        if not usuarios.exists() or not articulos.exists():
            self.stdout.write(self.style.ERROR('No existen usuarios o artículos en la base de datos.'))
            return

        # Crear algunas reservas de ejemplo
        for i in range(5):
            # Seleccionar un usuario y un artículo al azar
            usuario = usuarios.order_by('?').first()
            articulo = articulos.order_by('?').first()

            # Crear una reserva con el usuario y artículo seleccionados
            Reserva.objects.create(
                usuari=usuario,
                article=articulo,
                data_reserva=datetime.now()
            )

        self.stdout.write(self.style.SUCCESS('Data seeded successfully'))
