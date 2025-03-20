from django.urls import path
from . import views  # Pastikan ini benar

urlpatterns = [
    path('', views.home, name='home'),  
    path('add/', views.add_alumni, name='add_alumni'),
    path('list/', views.list_alumni, name='list_alumni'),
    path('edit/<int:id>/', views.edit_alumni, name='edit_alumni'),
    path('delete/<int:id>/', views.delete_alumni, name='delete_alumni'),
]
