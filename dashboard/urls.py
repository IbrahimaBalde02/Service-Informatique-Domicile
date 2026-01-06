from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.redirect_dashboard, name='redirect'),
    path('client/', views.dashboard_client, name='client'),
    path('prestataire/', views.dashboard_prestataire, name='prestataire'),
]