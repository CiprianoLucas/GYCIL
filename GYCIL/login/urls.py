from django.urls import path
from . import views

app_name = "login"
urlpatterns = [
    path('users/', views.UserLoginView.as_view(), name='user_login'),
    path('company/', views.CompanyLoginView.as_view(), name='company_login'),
]