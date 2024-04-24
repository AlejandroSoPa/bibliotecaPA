from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from biblioteca.models import Prestec, Usuari, Article
from datetime import datetime

class Command(BaseCommand):
    help = 'Seed the database with dummy data for Prestec model'

    def handle(self, *args, **kwargs):
        # Obtener algunos usuarios y artículos existentes para asignar a los préstamos
        usuarios = Usuari.objects.all()
        articulos = Article.objects.all()

        if not usuarios.exists() or not articulos.exists():
            self.stdout.write(self.style.ERROR('No existen usuarios o artículos en la base de datos.'))
            return

        # Crear algunos préstamos de ejemplo
        for i in range(5):
            # Seleccionar un usuario y un artículo al azar
            usuario = usuarios.order_by('?').first()
            articulo = articulos.order_by('?').first()

            # Crear un préstamo con el usuario y artículo seleccionados
            Prestec.objects.create(
                usuari=usuario,
                article=articulo,
                data_préstec=datetime.now(),
                data_retorn=None
            )

        self.stdout.write(self.style.SUCCESS('Data seeded successfully for Prestec model'))