from django.core.management.base import BaseCommand
from biblioteca.models import Llibre
from datetime import datetime

class Command(BaseCommand):
    help = 'Seed the database with dummy data for Llibre model'

    def handle(self, *args, **kwargs):
        autors = {
            "Harry Potter i la pedra filosofal": "J.K. Rowling",
            "Harry Potter i la cambra secreta": "J.K. Rowling",
            "Harry Potter i el pres d'Azkaban": "J.K. Rowling",
            "Harry Potter i el calze de foc": "J.K. Rowling",
            "Harry Potter i l'orde del Fènix": "J.K. Rowling",
            "Harry Potter i el príncep mestís": "J.K. Rowling",
            "Harry Potter i les relíquies de la Mort": "J.K. Rowling",
            "Geronimo Stilton: El secret dels cavallers": "Geronimo Stilton",
            "Geronimo Stilton: El tresor de l'illa del corall": "Geronimo Stilton",
            "Geronimo Stilton: El misteri del tresor desaparegut": "Geronimo Stilton",
            "Geronimo Stilton: La llegenda dels cavallers de l'Espai": "Geronimo Stilton",
            "Geronimo Stilton: L'aventura més dolça": "Geronimo Stilton",
            "Geronimo Stilton: La gran cursa de ratzingers": "Geronimo Stilton",
            "Geronimo Stilton: El gran llibre de les invencions": "Geronimo Stilton",
            "Percy Jackson i el lladre del llamp": "Rick Riordan",
            "Percy Jackson i el mar de monstres": "Rick Riordan",
            "Percy Jackson i la maledicció del tità": "Rick Riordan",
            "Percy Jackson i la batalla del laberint": "Rick Riordan",
            "Percy Jackson i els Déus de l'Olimp: El lladre de llamps": "Rick Riordan",
            "Percy Jackson i els Déus de l'Olimp: El mar de monstres": "Rick Riordan",
            "Percy Jackson i els Déus de l'Olimp: La maldició del tità": "Rick Riordan",
            "Percy Jackson i els Déus de l'Olimp: La batalla del laberint": "Rick Riordan"
        }
        
        editors = {
            "Harry Potter i la pedra filosofal": "Bloomsbury Publishing",
            "Harry Potter i la cambra secreta": "Bloomsbury Publishing",
            "Harry Potter i el pres d'Azkaban": "Bloomsbury Publishing",
            "Harry Potter i el calze de foc": "Bloomsbury Publishing",
            "Harry Potter i l'orde del Fènix": "Bloomsbury Publishing",
            "Harry Potter i el príncep mestís": "Bloomsbury Publishing",
            "Harry Potter i les relíquies de la Mort": "Bloomsbury Publishing",
            "Geronimo Stilton: El secret dels cavallers": "Ediciones B",
            "Geronimo Stilton: El tresor de l'illa del corall": "Ediciones B",
            "Geronimo Stilton: El misteri del tresor desaparegut": "Ediciones B",
            "Geronimo Stilton: La llegenda dels cavallers de l'Espai": "Ediciones B",
            "Geronimo Stilton: L'aventura més dolça": "Ediciones B",
            "Geronimo Stilton: La gran cursa de ratzingers": "Ediciones B",
            "Geronimo Stilton: El gran llibre de les invencions": "Ediciones B",
            "Percy Jackson i el lladre del llamp": "Scholastic Corporation",
            "Percy Jackson i el mar de monstres": "Scholastic Corporation",
            "Percy Jackson i la maledicció del tità": "Scholastic Corporation",
            "Percy Jackson i la batalla del laberint": "Scholastic Corporation",
            "Percy Jackson i els Déus de l'Olimp: El lladre de llamps": "Scholastic Corporation",
            "Percy Jackson i els Déus de l'Olimp: El mar de monstres": "Scholastic Corporation",
            "Percy Jackson i els Déus de l'Olimp: La maldició del tità": "Scholastic Corporation",
            "Percy Jackson i els Déus de l'Olimp: La batalla del laberint": "Scholastic Corporation"
        }
        
        col·leccions = {
            "Harry Potter i la pedra filosofal": "Sèrie Harry Potter",
            "Harry Potter i la cambra secreta": "Sèrie Harry Potter",
            "Harry Potter i el pres d'Azkaban": "Sèrie Harry Potter",
            "Harry Potter i el calze de foc": "Sèrie Harry Potter",
            "Harry Potter i l'orde del Fènix": "Sèrie Harry Potter",
            "Harry Potter i el príncep mestís": "Sèrie Harry Potter",
            "Harry Potter i les relíquies de la Mort": "Sèrie Harry Potter",
            "Geronimo Stilton: El secret dels cavallers": "Geronimo Stilton Series",
            "Geronimo Stilton: El tresor de l'illa del corall": "Geronimo Stilton Series",
            "Geronimo Stilton: El misteri del tresor desaparegut": "Geronimo Stilton Series",
            "Geronimo Stilton: La llegenda dels cavallers de l'Espai": "Geronimo Stilton Series",
            "Geronimo Stilton: L'aventura més dolça": "Geronimo Stilton Series",
            "Geronimo Stilton: La gran cursa de ratzingers": "Geronimo Stilton Series",
            "Geronimo Stilton: El gran llibre de les invencions": "Geronimo Stilton Series",
            "Percy Jackson i el lladre del llamp": "Percy Jackson Series",
            "Percy Jackson i el mar de monstres": "Percy Jackson Series",
            "Percy Jackson i la maledicció del tità": "Percy Jackson Series",
            "Percy Jackson i la batalla del laberint": "Percy Jackson Series",
            "Percy Jackson i els Déus de l'Olimp: El lladre de llamps": "Percy Jackson Series",
            "Percy Jackson i els Déus de l'Olimp: El mar de monstres": "Percy Jackson Series",
            "Percy Jackson i els Déus de l'Olimp: La maldició del tità": "Percy Jackson Series",
            "Percy Jackson i els Déus de l'Olimp: La batalla del laberint": "Percy Jackson Series"
        }
        
        pagines = {
            "Harry Potter i la pedra filosofal": 256,
            "Harry Potter i la cambra secreta": 288,
            "Harry Potter i el pres d'Azkaban": 348,
            "Harry Potter i el calze de foc": 636,
            "Harry Potter i l'orde del Fènix": 816,
            "Harry Potter i el príncep mestís": 704,
            "Harry Potter i les relíquies de la Mort": 792,
            "Geronimo Stilton: El secret dels cavallers": 128,
            "Geronimo Stilton: El tresor de l'illa del corall": 128,
            "Geronimo Stilton: El misteri del tresor desaparegut": 128,
            "Geronimo Stilton: La llegenda dels cavallers de l'Espai": 128,
            "Geronimo Stilton: L'aventura més dolça": 128,
            "Geronimo Stilton: La gran cursa de ratzingers": 128,
            "Geronimo Stilton: El gran llibre de les invencions": 128,
            "Percy Jackson i el lladre del llamp": 377,
            "Percy Jackson i el mar de monstres": 377,
            "Percy Jackson i la maledicció del tità": 381,
            "Percy Jackson i la batalla del laberint": 400,
            "Percy Jackson i els Déus de l'Olimp: El lladre de llamps": 375,
            "Percy Jackson i els Déus de l'Olimp: El mar de monstres": 375,
            "Percy Jackson i els Déus de l'Olimp: La maldició del tità": 375,
            "Percy Jackson i els Déus de l'Olimp: La batalla del laberint": 381
        }

        ISBNs = {
            "Harry Potter i la pedra filosofal": "9788478884454",
            "Harry Potter i la cambra secreta": "9788478884454",
            "Harry Potter i el pres d'Azkaban": "9788478884454",
            "Harry Potter i el calze de foc": "9788478884454",
            "Harry Potter i l'orde del Fènix": "9788478884454",
            "Harry Potter i el príncep mestís": "9788478884454",
            "Harry Potter i les relíquies de la Mort": "9788478884454",
            "Geronimo Stilton: El secret dels cavallers": "9788424657304",
            "Geronimo Stilton: El tresor de l'illa del corall": "9788424666757",
            "Geronimo Stilton: El misteri del tresor desaparegut": "9788424651920",
            "Geronimo Stilton: La llegenda dels cavallers de l'Espai": "9788424651920",
            "Geronimo Stilton: L'aventura més dolça": "9788424651920",
            "Geronimo Stilton: La gran cursa de ratzingers": "9788424651920",
            "Geronimo Stilton: El gran llibre de les invencions": "9788424651920",
            "Percy Jackson i el lladre del llamp": "9780141346809",
            "Percy Jackson i el mar de monstres": "9780141346809",
            "Percy Jackson i la maledicció del tità": "9780141346809",
            "Percy Jackson i la batalla del laberint": "9780141346809",
            "Percy Jackson i els Déus de l'Olimp: El lladre de llamps": "9780141346809",
            "Percy Jackson i els Déus de l'Olimp: El mar de monstres": "9780141346809",
            "Percy Jackson i els Déus de l'Olimp: La maldició del tità": "9780141346809",
            "Percy Jackson i els Déus de l'Olimp: La batalla del laberint": "9780141346809"
        }

        cdu_values = {
            "Harry Potter i la pedra filosofal": "823.914-9",
            "Harry Potter i la cambra secreta": "823.914-9",
            "Harry Potter i el pres d'Azkaban": "823.914-9",
            "Harry Potter i el calze de foc": "823.914-9",
            "Harry Potter i l'orde del Fènix": "823.914-9",
            "Harry Potter i el príncep mestís": "823.914-9",
            "Harry Potter i les relíquies de la Mort": "823.914-9",
            "Geronimo Stilton: El secret dels cavallers": "853",
            "Geronimo Stilton: El tresor de l'illa del corall": "853",
            "Geronimo Stilton: El misteri del tresor desaparegut": "853",
            "Geronimo Stilton: La llegenda dels cavallers de l'Espai": "853",
            "Geronimo Stilton: L'aventura més dolça": "853",
            "Geronimo Stilton: La gran cursa de ratzingers": "853",
            "Geronimo Stilton: El gran llibre de les invencions": "853",
            "Percy Jackson i el lladre del llamp": "823.914-9",
            "Percy Jackson i el mar de monstres": "823.914-9",
            "Percy Jackson i la maledicció del tità": "823.914-9",
            "Percy Jackson i la batalla del laberint": "823.914-9",
            "Percy Jackson i els Déus de l'Olimp: El lladre de llamps": "823.914-9",
            "Percy Jackson i els Déus de l'Olimp: El mar de monstres": "823.914-9",
            "Percy Jackson i els Déus de l'Olimp: La maldició del tità": "823.914-9",
            "Percy Jackson i els Déus de l'Olimp: La batalla del laberint": "823.914-9"
        }

        fechas_publicacion = {
            "Harry Potter i la pedra filosofal": "1999-06-26",
            "Harry Potter i la cambra secreta": "1998-07-02",
            "Harry Potter i el pres d'Azkaban": "1999-07-08",
            "Harry Potter i el calze de foc": "2000-07-08",
            "Harry Potter i l'orde del Fènix": "2003-06-21",
            "Harry Potter i el príncep mestís": "2005-07-16",
            "Harry Potter i les relíquies de la Mort": "2007-07-21",
            "Geronimo Stilton: El secret dels cavallers": "2010-03-15",
            "Geronimo Stilton: El tresor de l'illa del corall": "2005-10-01",
            "Geronimo Stilton: El misteri del tresor desaparegut": "2002-01-01",
            "Geronimo Stilton: La llegenda dels cavallers de l'Espai": "2006-06-01",
            "Geronimo Stilton: L'aventura més dolça": "2012-04-01",
            "Geronimo Stilton: La gran cursa de ratzingers": "2011-09-01",
            "Geronimo Stilton: El gran llibre de les invencions": "2011-03-01",
            "Percy Jackson i el lladre del llamp": "2005-06-28",
            "Percy Jackson i el mar de monstres": "2006-04-01",
            "Percy Jackson i la maledicció del tità": "2007-05-01",
            "Percy Jackson i la batalla del laberint": "2008-05-06",
            "Percy Jackson i els Déus de l'Olimp: El lladre de llamps": "2005-06-28",
            "Percy Jackson i els Déus de l'Olimp: El mar de monstres": "2006-04-01",
            "Percy Jackson i els Déus de l'Olimp: La maldició del tità": "2007-05-01",
            "Percy Jackson i els Déus de l'Olimp: La batalla del laberint": "2008-05-06"
        }

        for titol, autor in autors.items():
            data_publicacio = datetime.strptime(fechas_publicacion[titol], '%Y-%m-%d').date()
            cdu = cdu_values[titol]
            editor = editors[titol]
            colleccio = col·leccions[titol]
            num_pagines = pagines[titol]
            isbn = ISBNs[titol]

            Llibre.objects.create(
                titol=titol,
                descripcio=f"Una aventura sobre {titol}",
                autor=autor,
                data_publicacio=data_publicacio,
                CDU=cdu,
                ISBN=isbn,
                editor=editor,
                colleccio=colleccio,
                pagines=num_pagines,
                signatura=f"{autor[0]}{num_pagines}"  # Usando el primer caracter del autor y el número de páginas para la signatura
            )

        self.stdout.write(self.style.SUCCESS('Data seeded successfully'))
