from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('canciones/', views.canciones, name='canciones'),
    path('autores/', views.autores, name='autores'),
    path('logout/', views.exit, name='exit'),
]