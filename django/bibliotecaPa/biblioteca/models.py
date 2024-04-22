from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuari(AbstractUser):
    admin = models.BooleanField(default=False)
    data_naixement = models.DateField()
    centre = models.ForeignKey('Centre', on_delete=models.CASCADE, null=True, blank=True)
    cicle = models.CharField(max_length=100, null=True, blank=True)
    imatge = models.ImageField(upload_to='fotos_perfil', default='default.jpg')

class Centre(models.Model):
    nom = models.CharField(max_length=128)

class Article(models.Model):
    titol = models.CharField(max_length=200)
    descripcio = models.TextField()
    autor = models.CharField(max_length=200)
    data_publicacio = models.DateField()
    imatge = models.ImageField(upload_to='imatges_cataleg', default='default.jpg', null=True, blank=True)

class Llibre(Article):
    CDU = models.CharField(max_length=100)
    ISBN = models.CharField(max_length=13)
    editor = models.CharField(max_length=100)
    colleccio = models.CharField(max_length=100)
    pagines = models.IntegerField()
    signatura = models.CharField(max_length=100)

class CD(Article):
    estil = models.CharField(max_length=100)
    discografia = models.CharField(max_length=100)
    durada = models.DurationField()

class DVD(Article):
    director = models.CharField(max_length=100)
    durada = models.DurationField()

class BR(Article):
    durada = models.DurationField()
    estudi = models.CharField(max_length=100)

class Dispositiu(Article):
    marca = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

class Reserva(models.Model):
    usuari = models.ForeignKey(Usuari, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    data_reserva = models.DateTimeField(auto_now_add=True)

class Prestec(models.Model):
    usuari = models.ForeignKey(Usuari, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    data_préstec = models.DateTimeField(auto_now_add=True)
    data_retorn = models.DateTimeField(null=True, blank=True)

class Solicitud(models.Model):
    usuari = models.ForeignKey(Usuari, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    data_sol·licitud = models.DateField(auto_now_add=True)
    text_sol·licitud = models.TextField()
    centre_solicitant = models.ForeignKey(Centre, on_delete=models.CASCADE, related_name="peticio_solicitant")

class Log(models.Model):
    esdeveniment = models.CharField(max_length=200)
    nivell = models.CharField(max_length=20)  
    data = models.DateTimeField(auto_now_add=True)
    usuari = models.ForeignKey(Usuari, on_delete=models.CASCADE)
    ruta = models.CharField(max_length=100)