from django.db import models
from django.utils import timezone

class ServiceRequest(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    SERVICE_CHOICES = [
        ('limpeza_residencial', 'Limpeza Residencial - Serviço de limpeza completa de residências, incluindo aspiração, limpeza de superfícies, banheiros, cozinha e remoção de poeira.'),
        ('manutencao_jardim', 'Manutenção de Jardim - Serviço de manutenção e cuidados com jardins, incluindo corte de grama, poda de plantas, remoção de ervas daninhas e fertilização.'),
        ('reparos_eletricos', 'Reparos Elétricos - Serviço de reparo e instalação elétrica em residências, incluindo troca de tomadas, interruptores, instalação de luminárias e solução de problemas elétricos simples.')
    ]
    service_choice = models.CharField(max_length=20, choices=SERVICE_CHOICES)
    accepted = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
