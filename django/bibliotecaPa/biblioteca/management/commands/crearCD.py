from django.core.management.base import BaseCommand
from biblioteca.models import CD
from datetime import timedelta, datetime

class Command(BaseCommand):
    help = 'Seed the database with dummy data for CD model'

    def handle(self, *args, **kwargs):
        autors = {
            "Dark Side of the Moon": "Pink Floyd",
            "Abbey Road": "The Beatles",
            "Thriller": "Michael Jackson",
            "The Wall": "Pink Floyd",
            "Back in Black": "AC/DC",
            "Led Zeppelin IV": "Led Zeppelin",
            "Sgt. Pepper's Lonely Hearts Club Band": "The Beatles",
            "Rumours": "Fleetwood Mac",
            "The White Album": "The Beatles",
            "Greatest Hits": "Queen",
            "Hotel California": "Eagles",
            "Nevermind": "Nirvana",
            "Born to Run": "Bruce Springsteen",
            "The Joshua Tree": "U2",
            "Exile on Main St.": "The Rolling Stones",
            "A Night at the Opera": "Queen",
            "Who's Next": "The Who",
            "Led Zeppelin II": "Led Zeppelin",
            "The Rise and Fall of Ziggy Stardust": "David Bowie",
            "The Doors": "The Doors",
            "A Day at the Races": "Queen",
            "Led Zeppelin III": "Led Zeppelin",
            "Are You Experienced": "The Jimi Hendrix Experience",
            "Goodbye Yellow Brick Road": "Elton John"
        }

        discografies = {
            "Dark Side of the Moon": "Harvest Records",
            "Abbey Road": "Apple Records",
            "Thriller": "Epic Records",
            "The Wall": "Columbia Records",
            "Back in Black": "Atlantic Records",
            "Led Zeppelin IV": "Atlantic Records",
            "Sgt. Pepper's Lonely Hearts Club Band": "Parlophone",
            "Rumours": "Warner Bros. Records",
            "The White Album": "Apple Records",
            "Greatest Hits": "EMI Records",
            "Hotel California": "Asylum Records",
            "Nevermind": "DGC Records",
            "Born to Run": "Columbia Records",
            "The Joshua Tree": "Island Records",
            "Exile on Main St.": "Rolling Stones Records",
            "A Night at the Opera": "EMI Records",
            "Who's Next": "Decca Records",
            "Led Zeppelin II": "Atlantic Records",
            "The Rise and Fall of Ziggy Stardust": "RCA Records",
            "The Doors": "Elektra Records",
            "A Day at the Races": "EMI Records",
            "Led Zeppelin III": "Atlantic Records",
            "Are You Experienced": "Track Records",
            "Goodbye Yellow Brick Road": "MCA Records"
        }

        durades = {
            "Dark Side of the Moon": timedelta(hours=42, minutes=57),
            "Abbey Road": timedelta(hours=47, minutes=23),
            "Thriller": timedelta(hours=42, minutes=19),
            "The Wall": timedelta(hours=1, minutes=20, seconds=43),
            "Back in Black": timedelta(hours=42, minutes=11),
            "Led Zeppelin IV": timedelta(hours=42, minutes=37),
            "Sgt. Pepper's Lonely Hearts Club Band": timedelta(hours=39, minutes=52),
            "Rumours": timedelta(hours=39, minutes=44),
            "The White Album": timedelta(hours=1, minutes=33, seconds=43),
            "Greatest Hits": timedelta(hours=58, minutes=49),
            "Hotel California": timedelta(hours=43, minutes=30),
            "Nevermind": timedelta(hours=44, minutes=48),
            "Born to Run": timedelta(hours=39, minutes=29),
            "The Joshua Tree": timedelta(hours=50, minutes=13),
            "Exile on Main St.": timedelta(hours=1, minutes=6, seconds=54),
            "A Night at the Opera": timedelta(hours=43, minutes=8),
            "Who's Next": timedelta(hours=43, minutes=47),
            "Led Zeppelin II": timedelta(hours=41, minutes=31),
            "The Rise and Fall of Ziggy Stardust": timedelta(hours=38, minutes=37),
            "The Doors": timedelta(hours=44, minutes=10),
            "A Day at the Races": timedelta(hours=44, minutes=45),
            "Led Zeppelin III": timedelta(hours=43, minutes=8),
            "Are You Experienced": timedelta(hours=40, minutes=50),
            "Goodbye Yellow Brick Road": timedelta(hours=1, minutes=16, seconds=22)
        }


        fechas_publicacion = {
            "Dark Side of the Moon": "1973-03-01",
            "Abbey Road": "1969-09-26",
            "Thriller": "1982-11-30",
            "The Wall": "1979-11-30",
            "Back in Black": "1980-07-25",
            "Led Zeppelin IV": "1971-11-08",
            "Sgt. Pepper's Lonely Hearts Club Band": "1967-06-01",
            "Rumours": "1977-02-04",
            "The White Album": "1968-11-22",
            "Greatest Hits": "1981-10-26",
            "Hotel California": "1976-12-08",
            "Nevermind": "1991-09-24",
            "Born to Run": "1975-08-25",
            "The Joshua Tree": "1987-03-09",
            "Exile on Main St.": "1972-05-12",
            "A Night at the Opera": "1975-11-21",
            "Who's Next": "1971-08-14",
            "Led Zeppelin II": "1969-10-22",
            "The Rise and Fall of Ziggy Stardust": "1972-06-16",
            "The Doors": "1967-01-04",
            "A Day at the Races": "1976-12-10",
            "Led Zeppelin III": "1970-10-05",
            "Are You Experienced": "1967-05-12",
            "Goodbye Yellow Brick Road": "1973-10-05"
        }

        estils = {
            "Dark Side of the Moon": "Rock Progresivo",
            "Abbey Road": "Rock Psicodélico",
            "Thriller": "Pop",
            "The Wall": "Rock Progresivo",
            "Back in Black": "Hard Rock",
            "Led Zeppelin IV": "Hard Rock",
            "Sgt. Pepper's Lonely Hearts Club Band": "Rock Psicodélico",
            "Rumours": "Pop Rock",
            "The White Album": "Rock",
            "Greatest Hits": "Rock",
            "Hotel California": "Rock",
            "Nevermind": "Grunge",
            "Born to Run": "Rock",
            "The Joshua Tree": "Rock",
            "Exile on Main St.": "Rock",
            "A Night at the Opera": "Rock",
            "Who's Next": "Rock",
            "Led Zeppelin II": "Hard Rock",
            "The Rise and Fall of Ziggy Stardust": "Rock",
            "The Doors": "Rock Psicodélico",
            "A Day at the Races": "Rock",
            "Led Zeppelin III": "Hard Rock",
            "Are You Experienced": "Rock Psicodélico",
            "Goodbye Yellow Brick Road": "Rock"
        }

        for titol, autor in autors.items():
            data_publicacio = datetime.strptime(fechas_publicacion[titol], '%Y-%m-%d').date()
            estil = estils[titol]
            discografia = discografies[titol]
            durada = durades[titol]

            CD.objects.create(
                titol=titol,
                descripcio=f"Un clásico de {autor}",
                autor=autor,
                data_publicacio=data_publicacio,
                estil=estil,
                discografia=discografia,
                durada=durada
            )

        self.stdout.write(self.style.SUCCESS('Data seeded successfully'))
