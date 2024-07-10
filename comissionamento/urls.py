from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    # Comissionamento
    path('comissionamento/', views.comissionamentos, name='comissionamentos'),
    path('comissionamento/cadastrar/', views.cadastrar_comissionamento, name='cadastrar_comissionamento'),
    path('comissionamento/<int:pk>/', views.detalhes_comissionamento, name='detalhes_comissionamento'),
    path('comissionamento/<int:pk>/editar', views.editar_comissionamento, name='editar_comissionamento'),
    path('comissionamento/<int:pk>/cancelar', views.cancelar_comissionamento, name='cancelar_comissionamento'),
    
    path('teste/', views.teste, name='teste'),
]