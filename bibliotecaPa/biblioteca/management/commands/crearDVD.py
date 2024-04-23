from django.core.management.base import BaseCommand
from biblioteca.models import DVD
from datetime import datetime, timedelta

class Command(BaseCommand):
    help = 'Seed the database with dummy data for DVD model'

    def handle(self, *args, **kwargs):
        titles = {
            "The Shawshank Redemption": "Frank Darabont",
            "The Godfather": "Francis Ford Coppola",
            "The Dark Knight": "Christopher Nolan",
            "12 Angry Men": "Sidney Lumet",
            "Schindler's List": "Steven Spielberg",
            "Pulp Fiction": "Quentin Tarantino",
            "The Lord of the Rings: The Return of the King": "Peter Jackson",
            "The Good, the Bad and the Ugly": "Sergio Leone",
            "Fight Club": "David Fincher",
            "Forrest Gump": "Robert Zemeckis",
            "Inception": "Christopher Nolan",
            "The Matrix": "Lana Wachowski, Lilly Wachowski",
            "Goodfellas": "Martin Scorsese",
            "City of God": "Fernando Meirelles, Kátia Lund",
            "Se7en": "David Fincher",
            "The Silence of the Lambs": "Jonathan Demme",
            "The Lord of the Rings: The Fellowship of the Ring": "Peter Jackson",
            "The Usual Suspects": "Bryan Singer",
            "Léon: The Professional": "Luc Besson",
            "The Pianist": "Roman Polanski"
        }
        
        directors = {
            "The Shawshank Redemption": "Frank Darabont",
            "The Godfather": "Francis Ford Coppola",
            "The Dark Knight": "Christopher Nolan",
            "12 Angry Men": "Sidney Lumet",
            "Schindler's List": "Steven Spielberg",
            "Pulp Fiction": "Quentin Tarantino",
            "The Lord of the Rings: The Return of the King": "Peter Jackson",
            "The Good, the Bad and the Ugly": "Sergio Leone",
            "Fight Club": "David Fincher",
            "Forrest Gump": "Robert Zemeckis",
            "Inception": "Christopher Nolan",
            "The Matrix": "Lana Wachowski, Lilly Wachowski",
            "Goodfellas": "Martin Scorsese",
            "City of God": "Fernando Meirelles, Kátia Lund",
            "Se7en": "David Fincher",
            "The Silence of the Lambs": "Jonathan Demme",
            "The Lord of the Rings: The Fellowship of the Ring": "Peter Jackson",
            "The Usual Suspects": "Bryan Singer",
            "Léon: The Professional": "Luc Besson",
            "The Pianist": "Roman Polanski"
        }
        
        durations = {
            "The Shawshank Redemption": "2:22:00",
            "The Godfather": "2:55:00",
            "The Dark Knight": "2:32:00",
            "12 Angry Men": "1:36:00",
            "Schindler's List": "3:15:00",
            "Pulp Fiction": "2:34:00",
            "The Lord of the Rings: The Return of the King": "3:21:00",
            "The Good, the Bad and the Ugly": "2:41:00",
            "Fight Club": "2:19:00",
            "Forrest Gump": "2:22:00",
            "Inception": "2:28:00",
            "The Matrix": "2:16:00",
            "Goodfellas": "2:25:00",
            "City of God": "2:10:00",
            "Se7en": "2:07:00",
            "The Silence of the Lambs": "1:58:00",
            "The Lord of the Rings: The Fellowship of the Ring": "2:58:00",
            "The Usual Suspects": "1:46:00",
            "Léon: The Professional": "1:50:00",
            "The Pianist": "2:30:00"
        }

        publication_dates = {
            "The Shawshank Redemption": "1994-10-14",
            "The Godfather": "1972-03-24",
            "The Dark Knight": "2008-07-18",
            "12 Angry Men": "1957-04-10",
            "Schindler's List": "1993-12-15",
            "Pulp Fiction": "1994-10-14",
            "The Lord of the Rings: The Return of the King": "2003-12-17",
            "The Good, the Bad and the Ugly": "1967-12-29",
            "Fight Club": "1999-10-15",
            "Forrest Gump": "1994-07-06",
            "Inception": "2010-07-16",
            "The Matrix": "1999-03-31",
            "Goodfellas": "1990-09-19",
            "City of God": "2002-08-30",
            "Se7en": "1995-09-22",
            "The Silence of the Lambs": "1991-02-14",
            "The Lord of the Rings: The Fellowship of the Ring": "2001-12-19",
            "The Usual Suspects": "1995-09-15",
            "Léon: The Professional": "1994-11-18",
            "The Pianist": "2002-09-24"
        }

        for title, director in titles.items():
            publication_date = datetime.strptime(publication_dates[title], '%Y-%m-%d').date()
            duration_str = durations[title]
            hours, minutes, seconds = map(int, duration_str.split(':'))
            duration = timedelta(hours=hours, minutes=minutes, seconds=seconds)

            DVD.objects.create(
                titol=title,
                descripcio=f"A masterpiece directed by {director}",
                autor=director,
                data_publicacio=publication_date,
                director=director,
                durada=duration
            )

        self.stdout.write(self.style.SUCCESS('Data seeded successfully'))
