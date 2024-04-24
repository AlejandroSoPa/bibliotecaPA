from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from biblioteca.models import Solicitud, Usuari, Article, Centre
from datetime import datetime

class Command(BaseCommand):
    help = 'Seed the database with dummy data for Solicitud model'

    def handle(self, *args, **kwargs):
        # Obtener algunos usuarios, artículos y centros existentes para las solicitudes
        usuarios = Usuari.objects.all()
        articulos = Article.objects.all()
        centros = Centre.objects.all()

        if not usuarios.exists() or not articulos.exists() or not centros.exists():
            self.stdout.write(self.style.ERROR('No existen usuarios, artículos o centros en la base de datos.'))
            return

        # Crear algunas solicitudes de ejemplo
        for i in range(5):
            # Seleccionar un usuario, un artículo y un centro al azar
            usuario = usuarios.order_by('?').first()
            articulo = articulos.order_by('?').first()
            centro = centros.order_by('?').first()

            # Crear una solicitud con el usuario, artículo y centro seleccionados
            Solicitud.objects.create(
                usuari=usuario,
                article=articulo,
                data_sol·licitud=datetime.now().date(),
                text_sol·licitud="Esta es una solicitud de ejemplo.",
                centre_solicitant=centro
            )

        self.stdout.write(self.style.SUCCESS('Data seeded successfully for Solicitud model'))