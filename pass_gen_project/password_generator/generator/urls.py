from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('password/', views.Password, name='password'),
    path('about/', views.about, name='about'),
]