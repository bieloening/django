from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.index, name='home'),
    path('adicionar/', views.adicionar, name='adicionar'),
    path('adicionar_tarefa/', views.adicionar_tarefa, name='adicionar_tarefa'),
    path('deletar/<int:id>/', views.deletar, name='deletar'),
    path('finalizar/<int:id>/', views.finalizar, name='finalizar'),
    path('editar/<int:id>/', views.editar, name='editar')
]