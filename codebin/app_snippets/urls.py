from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<slug:slug>/', views.edit_or_retrieve, name='edit_or_retrieve'),
]
