from django.urls import path
from . import views


app_name = 'services'

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('services/', views.liste_services, name='services'),
     path('contact/', views.contact_view, name='contact'),
    path('apropos/', views.apropos, name='apropos'),
]
