from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm

def login_view(request):
    error_message = None  # Definindo a variável error_message com None inicialmente

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            senha = form.cleaned_data['senha']
            user = authenticate(request, email=email, senha=senha)
            if user is not None:
                login(request, user)
                return redirect('companies:create')  
            else:
                error_message = 'Credenciais inválidas. Por favor, tente novamente.'
        else:
            error_message = 'Por favor, corrija os erros no formulário.'
    else:
        form = LoginForm()
    return render(request, 'auth/login.html', {'form': form, 'error_message': error_message})
