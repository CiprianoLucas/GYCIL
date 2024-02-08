from django.urls import path
from . import views

app_name = "companies"
urlpatterns = [
    path("", views.index, name="index"),
    path("cadastro/", views.create, name="create"),
    path("<str:category>/", views.companies_with_category, name="companies_with_category"),
]
