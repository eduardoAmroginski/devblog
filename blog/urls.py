from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sobre/', views.sobre_nos, name='sobre_nos'),
    path('artigo/<int:id>/', views.artigo_detalhe, name='detalhe_artigo'),
    path('contato/', views.fale_conosco, name='fale_conosco'),

    path('api/artigos/', views.api_listar_artigos, name='api_artigos'),
    path('api/artigos/novo/', views.api_criar_artigo, name='api_criar_artigo'),
]

