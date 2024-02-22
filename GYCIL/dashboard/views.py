from django.shortcuts import render
from .models import DataModel

def dashboard(request):
    # Lógica para recuperar os dados do modelo e passar para o template
    data = DataModel.objects.all()
    return render(request, 'dashboard.html', {'data': data})