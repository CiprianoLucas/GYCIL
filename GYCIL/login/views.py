from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.urls import reverse
from django.contrib.auth.views import LoginView

class UserLoginView(LoginView):
    template_name = "auth/loginUser.html"
    next_page = 'companies:index'
    redirect_authenticated_user = True


def mostrar_pagina_login_user(request, error_message=None):
    return render(request, 'loginUser.html', {'error_message': error_message})
    

def login_user(request):
    if request.method == 'POST':
        email_user = request.POST.get('email_user')
        password_user = request.POST.get('password_user')
        user = authenticate(request, email_user=email_user, password_user=password_user)
        
        if user is not None:
            login(request, user)
            return redirect('companies:index')
        else:
            error_message = "Email ou senha incorretos. Por favor, tente novamente."
            return mostrar_pagina_login_user(request, error_message)
    else:
        return mostrar_pagina_login_user(request)
        

def mostrar_pagina_login_company(request, error_message=None):
    return render(request, 'loginCompany.html', {'error_message': error_message})
    
def login_company(request):
    if request.method == 'POST':
        email_company = request.POST.get('email_company')
        cnpj = request.POST.get('cnpj')
        password_company = request.POST.get('password_company')
        company = authenticate(request, email_company=email_company, cnpj=cnpj, password_company=password_company)

        if company is not None:
            login(request, company)
            return HttpResponse('Login realizado com sucesso!')
        else:
            error_message = "Email ou senha incorretos. Por favor, tente novamente."
            return mostrar_pagina_login_company(request, error_message)
    else:
        return mostrar_pagina_login_company(request)
