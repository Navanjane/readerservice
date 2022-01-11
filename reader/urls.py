from django.urls import path
from .views import readpost

urlpatterns = [
    path('readpost/<int:pk>/', readpost),
]