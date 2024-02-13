from .forms import UserForm, ClientForm
from .models import Client
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserForm, ClientForm, UserClientForm


# Create your views here.
def index(request):
    users = Client.objects.all(). order_by('-id')
    
    context = {
        "users": users
    }
    
    return render(request, 'index.html', context)

def create(request):
       
    if request.method == 'POST':
        form = UserClientForm(request.POST)

        if form.is_valid():
            user_form = form.cleaned_data['user_form']
            client_form = form.cleaned_data['client_form']
            user = user_form.save()            
            client = client_form.save(commit=False)
            client.user = user
            client.save()
            messages.success(request, 'Cliente cadastrado')
            return redirect('companies:index')
        
        context = {
        'form': form,
        }
        
        return render(request, 'clients/create.html', context)
            
    
    form = UserClientForm
    
    context = {
        'form': form,
    }
    
    return render(request, 'clients/create.html', context)

def login(request):
    return render(request, "clients/login.html")
