from multiprocessing import context
from os import stat
from django.http import HttpResponse
from django.shortcuts import render,redirect
from admindepaginas.models import Soal, Jawabanpeserta, Peserta
import random
from admindepaginas.forms import CreateSoalForm, CreateJawabanpesertaForm, CreatePesertaForm


# Create your views here.

def homeuser(request):
    context = {
    }
    return render(request, 'userdepaginas/homeuser.html', context)


def evaluasi(request):

    if request.method == 'GET':
      soal = list(Soal.objects.all())
      jumlah_soal = 2
      acak = random.sample(soal, jumlah_soal)
      context = {
          'soal' : acak
      }
      return render(request, 'userdepaginas/evaluasi.html', context)

    if request.method == 'POST':
        data=request.POST
        if data['choice1'] == data['key1']:
            stat1=True  
            score1=2
        
        else:
            stat1=False
            score1=1
            

        if data['choice2'] == data['key2']:
            stat2=True
            score2=2
           
        else:
            stat2=False
            score2=1
           
        Totalscore=score1+score2
        

        ret=Jawabanpeserta.objects.create(idEH=data[''], pregunta=data['soal1'], nama=data['Akhwat'], jawaban=data['choice1'], larespuesta=data['key1'], score1=score1, score=Totalscore )
        ret=Jawabanpeserta.objects.create(pregunta=data['soal2'], nama=data['Akhwat'], jawaban=data['choice2'], larespuesta=data['key2'], score2=score2, score=Totalscore )
        return redirect('hasiljawaban')
    return render(request, 'userdepaginas/evaluasi.html')




def hasiljawaban(request):
    jawabanuser = Jawabanpeserta.objects.all().order_by('-id')[:2]
    context = {
        'jawabanuser' : jawabanuser
    }
    return render(request, 'userdepaginas/hasiljawaban.html', context)


def arsip(request):
    arsip = Jawabanpeserta.objects.all()

    context = {
        'arsip': arsip   
    }
    return render(request, 'userdepaginas/arsip.html', context)


def peserta(request):
    peserta = Peserta.objects.all()

    context = {
        'peserta': peserta
    }

    return render(request, 'userdepaginas/evaluasi.html', context)