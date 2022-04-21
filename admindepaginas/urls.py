from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.homeadmin, name='homeadmin'),
    path('addsoal/', views.addsoal, name='addsoal'),
    re_path(r'^edit/(?P<id>\d+)/$', views.edit, name='edit'),
    re_path(r'^(?P<id>\d+)/$', views.delete, name='delete'),
    
]
