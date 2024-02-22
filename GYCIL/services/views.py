from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.core.paginator import Paginator
from django.contrib import messages
from .models import Service
from companies.models import Company
from django.db import transaction
from django.http import JsonResponse
# Create your views here.

def index(request):
    
    form_action = reverse("services:index")
    services = Service.objects.order_by("-id")
    user_id = request.user.id
    if user_id:
        company = Company.objects.filter(id=user_id)
        categories_company = company.categories
        print(categories_company)

    paginator = Paginator(services, 30)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "services": page_obj,
        "form_action": form_action
    }

    return render(request, "services/index.html", context)

def refuse_service(request):
    service = get_object_or_404(Service, pk=id)
    company = get_object_or_404(Company, pk=id)
    service.delete()
    
    with transaction.atomic():
        service.companies_refused.add(company)
    service.save()
    
    return redirect("services:index")

def my_services_client(request):
    form_action = reverse("services:my_services_client")
    services = Service.objects.order_by("-id")
    user_id = request.user.id
    if user_id:
        company = Company.objects.filter(id=user_id)
        categories_company = company.categories
        print(categories_company)

    paginator = Paginator(services, 30)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "services": page_obj.object_list,
        "form_action": form_action
    }

    return render(request, "services/index.html", context)

def my_services_company(request):
    form_action = reverse("services:my_services_company")
    services = Service.objects.order_by("-id")
    user_id = request.user.id
    if user_id:
        company = Company.objects.filter(id=user_id)
        categories_company = company.categories
        print(categories_company)

    paginator = Paginator(services, 30)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "services": page_obj.object_list,
        "form_action": form_action
    }

    return render(request, "services/index.html", context)

def descriptions(request, id):
    service = Service.objects.filter(id=id).order_by('-id')
       
    service_serialized = [{
        'id': str(descriptions.id),
        'street': descriptions.street,
        'description': descriptions.description,
        'cep': descriptions.cep,
        'state': descriptions.state,
        'city': descriptions.city,
        'created_at': str(descriptions.created_at),
        'client': descriptions.client.name,
        'category': descriptions.category.name,
        
    } for descriptions in service]
    
    print(service_serialized)
    
    return JsonResponse(service_serialized, safe=False)