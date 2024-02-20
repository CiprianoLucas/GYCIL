from django.urls import path
from . import views


app_name = "login"
urlpatterns = [
    path('users/', views.UserLoginView.as_view(), name='login'),
    path('company/', views.login_company, name='login')   
]
