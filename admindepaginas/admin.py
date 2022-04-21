from django.contrib import admin
from .models import Peserta, Soal, Jawabanpeserta

# Register your models here.
admin.site.register(Soal)
admin.site.register(Peserta)
admin.site.register(Jawabanpeserta)
