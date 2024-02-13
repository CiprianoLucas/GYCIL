from django.shortcuts import render, get_list_or_404, redirect
from django.urls import reverse
from django.core.paginator import Paginator
from .forms import CompanyForm
from django.contrib import messages
from .forms import UserForm

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
        form = CompanyForm(request.POST)
        user_form = UserForm(request.POST)
        
        if form.is_valid() and user_form.is_valid():
            
            user_form.save()
            
            form.save()
            
            
            messages.success(request, 'Empresa cadastrada')
            
            return redirect('companies:index')
        
        context = {
        'form': form,
        'user_form': user_form,
        }
        
        return render(request, 'companies/create.html', context)
            
    
    form = CompanyForm()
    user_form = UserForm()
    
    context = {
        'form': form,
        'user_form': user_form,
    }
    
    return render(request, 'companies/create.html', context)