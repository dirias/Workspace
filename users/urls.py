from os import name
from django.urls import path
from users import views

urlpatterns = [
    path('', views.login, name='home'),
    path('login/', views.LoginView.as_view(), name='login'),
]