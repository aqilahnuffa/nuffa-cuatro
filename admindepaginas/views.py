from django.shortcuts import render

from admindepaginas.bank_soal.pertanyaan import banksoal


# Create your views here.
def homeadmin(request):
    bank_soal = banksoal()

    return render(request, 'admindepaginas/homeadmin.html', {'soal': bank_soal})