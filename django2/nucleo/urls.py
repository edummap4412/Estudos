from django.urls import path

from .views import conteudo, index, produto

urlpatterns = [
    path('conteudo', conteudo),
    path('index', index,name ='index'),
    path('produto/<int:id>', produto, name='produto'),

]
