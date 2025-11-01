from django.urls import path
from . import views
urlpatterns = [
    path('index/', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('happiness/', views.happiness, name='happiness'),
    path('economy/', views.economy, name='economy'),
    path('family/', views.family, name='family'),
    path('health/', views.health, name='health'),
    path('freedom/', views.freedom, name='freedom'),
    path('trust/', views.trust, name='trust'),
    path('generosity/', views.generosity, name='generosity'),
]