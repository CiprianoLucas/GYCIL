from django.shortcuts import render, get_list_or_404, redirect
from django.urls import reverse
from django.core.paginator import Paginator
from .forms import CompanyForm, UserForm
from django.contrib import messages

from .models import Company

# Create your views here.
def index(request):
    companies = Company.objects.order_by("-id")

    # Aplicando a paginação
    paginator = Paginator(companies, 30)
    # /fornecedores?page=1 -> Obtendo a página da URL
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    lines = len(page_obj.object_list) // 3
    if len(page_obj.object_list) % 3 != 0:
        lines += 1

    context = {
        "companies": page_obj.object_list,
        "lines": lines,
    }

    return render(request, "companies/index.html", context)


def companies_with_category(request):
    companies = Company.objects.order_by("-id")
        
    # Aplicando a paginação
    paginator = Paginator(companies, 2)
    # /fornecedores?page=1 -> Obtendo a página da URL
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    
    context = { "companies": page_obj }
    
    return render(request, "companies/index.html", context)

def create(request):
       
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        company_form = CompanyForm(request.POST, request.FILES)

        if user_form.is_valid() and company_form.is_valid():
                       
            user = user_form.save()
            client = company_form.save(commit=False)
            client.user = user
            client.save()
            messages.success(request, 'Cliente cadastrado')
            return redirect('companies:index')
        
        context = {
        'user_form': user_form,
        'company_form': company_form
        }
        
        return render(request, 'companies/create.html', context)
            
    
    user_form = UserForm()
    company_form = CompanyForm()
    
    context = {
    'user_form': user_form,
    'company_form': company_form
    }
    
    return render(request, 'companies/create.html', context)