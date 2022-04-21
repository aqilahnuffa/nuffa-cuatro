from django.db import models
from datetime import date

# Create your models here.

class Soal(models.Model):
    idEH = models.CharField(max_length=50, default='')
    pregunta = models.TextField()
    ellecion_uno = models.TextField()
    ellecion_dos = models.TextField()
    ellecion_tres = models.TextField()
    ellecion_cuatro = models.TextField()
    ANS = (('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'))
    larespuesta = models.CharField(max_length=1, null=True, choices=ANS)

    def __str__(self):
        return self.pregunta


class Peserta(models.Model):
    nama = models.TextField()
    NIP= models.CharField(max_length=100)
    def __str__(self):
        return self.nama


class Jawabanpeserta(models.Model):
    score = models.IntegerField(default=0)
    score1 = models.IntegerField(default=0)
    score2 = models.IntegerField(default=0) 
    
    pregunta=models.TextField()
    nama=models.TextField()
    jawaban = models.TextField()
    larespuesta = models.CharField(max_length=1, null=True)

    def __str__(self):
        return self.nama
    def __str__(self):
        return self.pregunta



