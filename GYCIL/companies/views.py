from django.shortcuts import render
from django.core.paginator import Paginator

from .models import Company

# Create your views here.
def index(request):
    companies = Company.objects.order_by("-id")
        
    # Aplicando a paginação
    paginator = Paginator(companies, 2)
    # /fornecedores?page=1 -> Obtendo a página da URL
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    
    context = { "companies": page_obj }
    
    return render(request, "companies/index.html", context)