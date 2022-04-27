from django.db import models
from datetime import date

# Create your models here.

class Soal(models.Model):
    ANS = (
        ('A', 'A'), ('B', 'B'), 
        ('C', 'C'), ('D', 'D')
    )
    
    pregunta = models.TextField()
    ellecion_uno = models.TextField()
    ellecion_dos = models.TextField()
    ellecion_tres = models.TextField()
    ellecion_cuatro = models.TextField()
    
    larespuesta = models.CharField(max_length=1, null=True, choices=ANS)

    def __str__(self):
        return self.pregunta


class Peserta(models.Model):
    nama = models.TextField()
    NIP= models.CharField(max_length=100)
    def __str__(self):
        return self.nama


class Jawabanpeserta(models.Model):
    idEH = models.CharField(max_length=50, default='')
    score = models.IntegerField(default=0)
    score1 = models.IntegerField(default=0)
    score2 = models.IntegerField(default=0) 
    pregunta=models.TextField()
    nama=models.TextField()
    is_true = models.BooleanField(default=False)
    jawaban = models.CharField(max_length=1)
    larespuesta = models.CharField(max_length=1, null=True)

    def __str__(self):
        return self.nama
    def __str__(self):
        return self.pregunta



