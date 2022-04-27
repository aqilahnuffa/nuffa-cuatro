
from operator import is_
from django.contrib import messages
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
            is_true = True  
            score1 = 2
        
        else:
            is_true = False
            score1 = 1
            

        if data['choice2'] == data['key2']:
            is_true = True
            score2=2
           
        else:
            is_true = False
            score2=1
           
        Totalscore=score1+score2
        
           
        

        ret=Jawabanpeserta.objects.create(idEH='', pregunta=data['soal1'], nama=data['Akhwat'], jawaban=data['choice1'], larespuesta=data['key1'], score1=score1, score=Totalscore, is_true=is_true) 
        ret=Jawabanpeserta.objects.create(idEH='', pregunta=data['soal2'], nama=data['Akhwat'], jawaban=data['choice2'], larespuesta=data['key2'], score2=score2, score=Totalscore, is_true=is_true )
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
    soal = Soal.objects.all()
    
    arsip_item = []
    for i in range(0, len(arsip), 2):

      arsip_item.append(arsip[i:i+2])
    
    context = {
        'arsip': arsip, 
        'arsip_item': arsip_item,
        'soal': soal
    }
    return render(request, 'userdepaginas/arsip.html', context)

def peserta(request):
    peserta = Peserta.objects.all()

    context = {
        'peserta': peserta
    }

    return render(request, 'userdepaginas/evaluasi.html', context)