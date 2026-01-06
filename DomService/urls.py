from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Services.urls', namespace='services')),
    path('comptes/', include('comptes.urls')),
    path('dashboard/', include('dashboard.urls', namespace='dashboard')),

]
