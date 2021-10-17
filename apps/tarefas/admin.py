from django.contrib import admin

# Register your models here.

from .models import Categoria, Tarefas

admin.site.register(Categoria)
admin.site.register(Tarefas)