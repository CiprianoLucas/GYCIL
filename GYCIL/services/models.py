from django.db import models
from django.utils.text import slugify
from companies.models import Company
from clients.models import Client

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(unique=True, blank=True)
    icon = models.ImageField(upload_to="icons_categories", blank=True, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        
class Service(models.Model):
    street = models.CharField(max_length=255)
    rating = models.CharField(max_length=255)
    number = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    date = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    hours_service = models.CharField(max_length=255)
    cep = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    neighbor = models.CharField(max_length=255)
    client = models.ForeignKey(Client, on_delete=models.DO_NOTHING)
    company = models.ForeignKey(Company, on_delete=models.DO_NOTHING)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    photos = models.FileField(upload_to="photos_services", blank=True, null=True)

    def __str__(self):
        return f"{self.client} - {self.company}"

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
