from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.auth import get_user_model
from biblioteca.models import Centre
from datetime import datetime
import os

User = get_user_model()

class Command(BaseCommand):
    help = 'Seed the database with dummy data for Usuari model'

    def handle(self, *args, **kwargs):
        # Crear algunos grupos de ejemplo si no existen
        if not Group.objects.exists():
            self.stdout.write(self.style.ERROR('No existen grupos en la base de datos.'))
            return

        # Obtener el grupo por defecto
        default_group = Group.objects.first()

        # Crear algunos usuarios de ejemplo
        for i in range(5):
            # Crear un usuario de ejemplo con datos aleatorios
            user = User.objects.create_user(
                username=f'user{i+1}',
                email=f'user{i+1}@example.com',
                password='password',
                admin=False,
                data_naixement=datetime.now().date(),
                centre=Centre.objects.order_by('?').first(),
                cicle='Cicle formatiu',
                imatge=self.get_random_image_path(),
            )

            # Asignar el usuario al grupo por defecto
            user.groups.add(default_group)

        self.stdout.write(self.style.SUCCESS('Data seeded successfully'))

    def get_random_image_path(self):
        # Directorio donde se encuentran las imágenes de ejemplo
        image_dir = 'path/to/your/image/directory'

        # Obtener una lista de las imágenes disponibles
        image_files = [f for f in os.listdir(image_dir) if os.path.isfile(os.path.join(image_dir, f))]

        # Seleccionar una imagen al azar de la lista
        if image_files:
            return os.path.join(image_dir, random.choice(image_files))
        else:
            return 'fotos_perfil/default.jpg'  # Si no hay imágenes disponibles, se usa una por defecto
