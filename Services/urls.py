from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),  # Page d'accueil
    path('Services/', views.liste_services, name='services'),
    path('contact/', views.contact, name='contact'),
    path('apropos/', views.apropos, name='apropos'),
]
