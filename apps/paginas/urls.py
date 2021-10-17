from django.urls import path

app_name = 'paginas'

from . import views

urlpatterns = [
    path('login/', views.fazer_login, name='fazer_login'),
    path('logout/', views.fazer_logout, name='fazer_logout'),
    path('', views.pagina_inicial, name='pagina_inicial'),
]