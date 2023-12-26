from django.urls import path
from apps.base import views

urlpatterns = [
    path('', views.index, name='home'),
    path('catalog/', views.catalog, name='catalog'),
    path('Genplaning', views.Gen_planing, name='genplaning')
]