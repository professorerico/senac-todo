from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import LoginForm

# Create your views here.
@login_required(login_url='/login/')
def pagina_inicial(request):
    template_name = 'paginas/pagina_inicial.html'
    context = {}
    return render(request, template_name, context)

def fazer_login(request):
    template_name = 'paginas/login.html'
    context = {}
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            usuario = form.cleaned_data['usuario']
            senha = form.cleaned_data['senha']
            usuario_obj = authenticate(username=usuario, password=senha)
            if usuario_obj is not None:
                if usuario_obj.is_active:
                    login(request, usuario_obj)
                    messages.success(request, 'Você esta logado')
                    return redirect('/')
                else:
                    messages.warning(request, 'Sua conta esta desativas')
                    return redirect('paginas:fazer_login')
            else:
                messages.warning(request, 'Usuário ou senha errada')
                return redirect('paginas:fazer_login')
        else:
            messages.error(request, "Erro ao acessar")
    else:
        form = LoginForm()
    context['form'] = form
    return render(request, template_name, context)

@login_required(login_url='/login/')
def fazer_logout(request):
    logout(request)
    messages.warning(request, 'Você foi desconectado')
    return redirect('paginas:fazer_login')

