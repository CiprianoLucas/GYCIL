from django.urls import path
from . import views

app_name = "companies"
urlpatterns = [
    path("index/", views.index, name="index"),
    path("cadastro/", views.create, name="create"),
]
