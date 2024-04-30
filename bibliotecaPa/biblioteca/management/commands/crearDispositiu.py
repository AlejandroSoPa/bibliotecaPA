from django.core.management.base import BaseCommand
from biblioteca.models import Dispositiu
from datetime import datetime

class Command(BaseCommand):
    help = 'Seed the database with dummy data for Dispositiu model'

    def handle(self, *args, **kwargs):
        articles = [
            {
                "titol": "Smartphone Galaxy S22",
                "descripcio": "El último smartphone de Samsung con características increíbles.",
                "autor": "Samsung",
                "data_publicacio": "2024-04-20",
                "imatge": "galaxy_s22.jpg",
                "marca": "Samsung",
                "model": "S22"
            },
            {
                "titol": "Laptop ThinkPad X1 Carbon",
                "descripcio": "Una laptop ultradelgada y ultraligera con potencia de clase empresarial.",
                "autor": "Lenovo",
                "data_publicacio": "2024-04-21",
                "imatge": "thinkpad_x1_carbon.jpg",
                "marca": "Lenovo",
                "model": "X1 Carbon"
            },
            {
                "titol": "Tablet iPad Pro",
                "descripcio": "La última tableta de Apple con un rendimiento increíble.",
                "autor": "Apple",
                "data_publicacio": "2024-04-22",
                "imatge": "ipad_pro.jpg",
                "marca": "Apple",
                "model": "iPad Pro"
            },
        ]

        for article_data in articles:
            # Convierte la cadena de fecha en un objeto de fecha
            data_publicacio = datetime.strptime(article_data['data_publicacio'], '%Y-%m-%d').date()

            Dispositiu.objects.create(
                titol=article_data['titol'],
                descripcio=article_data['descripcio'],
                autor=article_data['autor'],
                data_publicacio=data_publicacio,
                imatge=article_data['imatge'],
                marca=article_data['marca'],
                model=article_data['model']
            )

        self.stdout.write(self.style.SUCCESS('Data seeded successfully'))
