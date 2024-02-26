from django.urls import path
from . import views

urlpatterns = [
    path('client/', views.client_page, name='client_page'),
    path('company/', views.company_page, name='company_page'),
    path('accept/<int:request_id>/', views.accept_service, name='accept_service'),
    path('service/<int:request_id>/', views.service_details, name='service_details'),
]
