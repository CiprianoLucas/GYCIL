from django.contrib import admin
from .models import ServiceRequest  # Importando o modelo ServicesRequest

# Registrando o modelo ServicesRequest no painel de administração
admin.site.register(ServiceRequest)
