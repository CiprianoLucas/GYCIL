from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.TextField()
    senha = models.CharField(max_length=100)