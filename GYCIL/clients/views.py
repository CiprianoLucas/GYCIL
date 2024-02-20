from .forms import UserForm, ClientForm
from .models import Client
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserForm


# Create your views here.
def index(request):
    users = Client.objects.all(). order_by('-id')
    
    context = {
        "users": users
    }
    
    return render(request, 'index.html', context)

def create(request):
       
    if request.method == 'POST':
        form = ClientForm(request.POST)
        user_form = UserForm(request.POST)
        
        if form.is_valid() and user_form.is_valid():
            form.save()
            user_form.save()
            
            messages.success(request, 'Empresa cadastrada')
            
            return redirect('companies:index')
        
        context = {
        'form': form,
        'user_form': user_form,
        }
        
        return render(request, 'clients/create.html', context)
            
    
    form = ClientForm()
    user_form = UserForm()
    
    context = {
        'form': form,
        'user_form': user_form,
    }
    
    return render(request, 'clients/create.html', context)

def login(request):
    return render(request, "clients/login.html")
