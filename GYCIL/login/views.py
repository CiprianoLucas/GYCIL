from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views import View
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from .forms import UserForm, CompanyForm

class UserLoginView(View):
    template_name = 'auth/loginUser.html'

    def get(self, request):
        form = UserForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = UserForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            senha = form.cleaned_data.get('senha')
            user = authenticate(request, email=email, senha=senha)
            if user is not None:
                login(request, user)
                return redirect(reverse_lazy('companies:index'))  # Redireciona para a página de índice das empresas após o login bem-sucedido
            else:
                messages.error(request, "Email ou senha incorretos. Por favor, tente novamente.")
        return render(request, self.template_name, {'form': form})

class CompanyLoginView(View):
    template_name = "auth/loginCompany.html"

    def get(self, request):
        form = CompanyForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = CompanyForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            cnpj = form.cleaned_data.get('cnpj')
            senha = form.cleaned_data.get('senha')
            company = authenticate(request, email=email, cnpj=cnpj, senha=senha)
            if company is not None:
                login(request, company)
                return redirect(reverse_lazy('companies:index'))  # Redireciona para a página de índice das empresas após o login bem-sucedido
            else:
                messages.error(request, "Email, CNPJ ou senha incorretos. Por favor, tente novamente.")
        return render(request, self.template_name, {'form': form})
