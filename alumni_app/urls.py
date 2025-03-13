from django.urls import path
from . import views  # Pastikan ini benar

urlpatterns = [
    path('', views.home, name='home'),  # Minimal harus ada satu path
]
