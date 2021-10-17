from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import CategoriaForm, TarefaForm
from .models import Categoria, Tarefas

# Create your views here.
# CRUD de categorias
@login_required(login_url='/login/')
def adicionar_categoria(request):
    template_name = 'tarefas/adicionar_categoria.html'
    context = {}
    if request.method == 'POST':
        form = CategoriaForm(request.POST) #dicionário : POST= {}
        if form.is_valid() :
            form.save()
            messages.success(request, 'Categoria adiciona com Sucesso')
            return redirect('tarefas:listar_categorias') # --> /tarefas/adicionar-categoria
    else:
        form = CategoriaForm()
    context['form'] = form
    return render(request, template_name, context)

@login_required(login_url='/login/')
def listar_categorias(request):
    template_name = 'tarefas/listar_categorias.html'
    categorias = Categoria.objects.all()
    context = {
        'categorias' : categorias,
    }
    return render(request, template_name, context)

@login_required(login_url='/login/')
def apagar_categoria(request, pk):
    try:
        # Categoria.objects.get(pk=pk).delete()
        categoria = get_object_or_404(Categoria, pk=pk)
        categoria.delete()
    except Categoria.DoesNotExist :
        return redirect('/')
    messages.warning(request,'Categoria apagada!')
    return redirect('tarefas:listar_categorias')

@login_required(login_url='/login/')
def editar_categoria(request, pk):
    template_name = 'tarefas/adicionar_categoria.html'
    categoria = get_object_or_404(Categoria, pk=pk)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            messages.success(request, 'Categoria modificada')
            return redirect('tarefas:listar_categorias')
    else:
        form = CategoriaForm(instance=categoria)
    context = {
        'form' : form
    }
    return render(request, template_name, context)

# CRUD de tarefas
@login_required(login_url='/login/')
def adicionar_tarefa(request):
    template_name = 'tarefas/adicionar_tarefa.html'
    context = {}
    if request.method == 'POST' :
        form = TarefaForm(request.POST)
        if form.is_valid() :
            form.save()
            messages.success(request, 'Tarefa adiciona com sucesso')
            return redirect('tarefas:listar_tarefas')
    else :
        form = TarefaForm()
    context['form'] = form
    return render(request, template_name, context)

@login_required(login_url='/login/')
def listar_tarefas(request):
    template_name = 'tarefas/listar_tarefas.html'
    tarefas = Tarefas.objects.all().exclude(status='CD')
    context = {
        'tarefas' : tarefas,
    }
    return render(request, template_name, context)

@login_required(login_url='/login/')
def editar_tarefa(request, pk) :
    template_name = 'tarefas/adicionar_tarefa.html'
    tarefa = get_object_or_404(Tarefas, pk=pk)
    if tarefa.status != 'CD':
        if request.method == 'POST':
            form = TarefaForm(request.POST, instance=tarefa)
            if form.is_valid():
                form.save()
                messages.success(request, 'Tarefa modificada')
                return redirect('tarefas:listar_tarefas')
        else:
            form = TarefaForm(instance=tarefa)
        context = {
            'form' : form,
        }
    else:
       return redirect('tarefas:listar_tarefas')
    return render(request, template_name, context)

@login_required(login_url='/login/')
def apagar_tarefa(request, pk) :
    tarefa = get_object_or_404(Tarefas, pk=pk)
    if tarefa.status != 'CD':
        try:
            tarefa.delete()
        except Tarefas.DoesNotExist :
            return redirect('/')
        messages.warning(request, 'Tarefa apagada')
    return redirect('tarefas:listar_tarefas')

@login_required(login_url='/login/')
def listar_concluidas(request):
    template_name= 'tarefas/listar_concluidas.html'
    tarefas = Tarefas.objects.filter(status='CD')
    context = {
        'tarefas' : tarefas,
    }
    return render(request, template_name, context)