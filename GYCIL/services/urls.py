from . import views
from django.urls import path

app_name = "services"
urlpatterns = [
    path("", views.index, name="index"),
    path("cliente", views.my_services_client, name="my_services_client"),
    path("empresa", views.my_services_company, name="my_services_company"),
    path("<int:id>/descricao/", views.descriptions, name = "descriptions"),
]
