from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from .models import Soal
from .forms import CreateSoalForm
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.
def homeadmin(request):
    soal = Soal.objects.order_by('-id')
    context = {
        'soal' : soal
    }
    return render(request, 'admindepaginas/homeadmin.html', context)

def addsoal(request):
    if request.method == 'POST':
        form = CreateSoalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homeadmin')
    else:
        form = CreateSoalForm()

    context = {
        'form' : form
    }

    return render(request, 'admindepaginas/addsoal.html', context)

def edit(request, id):
    soal = Soal.objects.get(id=id)
    form = CreateSoalForm(instance=soal)

    if request.method == 'POST':
        form = CreateSoalForm(request.POST, instance=soal)
        if form.is_valid():
            form.save()
            return redirect('homeadmin')

    context = {
        'form' : form
    }
    return render(request, 'admindepaginas/edit.html', context)



def delete(request, id):
    try:
        Soal.objects.get(id=id).delete()
        return redirect('homeadmin')
    except ObjectDoesNotExist:
        return redirect('homeadmin')




