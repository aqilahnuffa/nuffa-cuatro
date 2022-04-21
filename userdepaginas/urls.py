from django.urls import path
from . import views

urlpatterns = [
    path('', views.homeuser, name='homeuser'),
    path('evaluasi/', views.evaluasi, name='evaluasi'),
    path('hasiljawaban/', views.hasiljawaban, name='hasiljawaban'),
    path('arsip/', views.arsip, name='arsip'),

]
