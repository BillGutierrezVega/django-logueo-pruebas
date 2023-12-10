from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('autores/', views.autores, name='autores'),
    path('logout/', views.exit, name='exit'),
]