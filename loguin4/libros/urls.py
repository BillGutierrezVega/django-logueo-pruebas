from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('libros/', views.libros, name='libros'),
    path('logout/', views.exit, name='exit'),
]