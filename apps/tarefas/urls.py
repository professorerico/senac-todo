from django.urls import path

app_name = 'tarefas'

from . import views

urlpatterns = [
    #categorias
    path('adicionar-categoria/', views.adicionar_categoria, name='adicionar_categoria'),
    path('listar-categorias/', views.listar_categorias, name='listar_categorias'),
    path('apagar-categoria/<int:pk>/', views.apagar_categoria, name='apagar_categoria'),
    path('editar-categoria/<int:pk>/', views.editar_categoria, name='editar_categoria'),
    #tarefas
    path('adicionar-tarefa/', views.adicionar_tarefa, name='adicionar_tarefa'),
    path('listar-tarefas/', views.listar_tarefas, name='listar_tarefas'),
    path('listar-tarefas-concluidas/', views.listar_concluidas, name='listar_concluidas'),
    path('apagar-tarefa/<int:pk>', views.apagar_tarefa, name='apagar_tarefa'),
    path('editar-tarefa/<int:pk>', views.editar_tarefa, name='editar_tarefa'),
    # path('', views.pagina_inicial, name='pagina_inicial'),
]
