from django.forms import ModelForm
from .models import Soal, Peserta, Jawabanpeserta

class CreateSoalForm(ModelForm):

    class Meta:
        model = Soal
        fields = ['pregunta', 'ellecion_uno', 'ellecion_dos', 'ellecion_tres', 'ellecion_cuatro', 'larespuesta']

class CreateJawabanpesertaForm(ModelForm):

    class Meta:
        model = Jawabanpeserta
        fields = ['score', 'pregunta', 'nama', 'jawaban']

class CreatePesertaForm(ModelForm):

    class Meta:
        model = Peserta
        fields = ['nama', 'NIP']
