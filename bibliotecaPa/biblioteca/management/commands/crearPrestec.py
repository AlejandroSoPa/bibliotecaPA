from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from biblioteca.models import Prestec, Usuari, Article
from datetime import datetime, timedelta
from django.utils import timezone
import random 

class Command(BaseCommand):
    help = 'Seed the database with dummy data for Prestec model'

    def handle(self, *args, **kwargs):
        # Obtener algunos usuarios y artículos existentes para asignar a los préstamos
        usuarios = Usuari.objects.all()
        articulos = Article.objects.filter(ejemplares__gt=0)  # Filtrar solo artículos con al menos un ejemplar

        if not usuarios.exists() or not articulos.exists():
            self.stdout.write(self.style.ERROR('No existen usuarios con ejemplares disponibles o artículos en la base de datos.'))
            return

        # Crear algunos préstamos de ejemplo
        for i in range(5):
            # Seleccionar un usuario y un artículo al azar
            usuario = usuarios.order_by('?').first()
            articulo = articulos.order_by('?').first()

            # Disminuir el número de ejemplares disponibles
            articulo.ejemplares -= 1
            articulo.save()

            data = timezone.now()
            
            # Calcular la fecha de préstamo sumando 2 horas
            data_prestec = data + timedelta(hours=2)
            data_lliurament = data_prestec + timedelta(days=random.randint(1, 40))
            # Calcular la fecha de retorno (fecha de préstamo + 30 días)
            data_retorn = data_prestec + timedelta(days=30)

            # Crear un préstamo con el usuario y artículo seleccionados
            Prestec.objects.create(
                usuari=usuario,
                article=articulo,
                data_préstec=data_prestec,
                data_lliurament=data_lliurament,
                data_retorn=data_retorn
            )

        self.stdout.write(self.style.SUCCESS('Data seeded successfully for Prestec model'))
