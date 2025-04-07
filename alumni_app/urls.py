from django.urls import path
from .views import (
    home, AlumniListView, AlumniDetailView, AlumniCreateView, AlumniUpdateView, AlumniDeleteView
)

urlpatterns = [
    path('', home, name='home'),
    path('alumni/', AlumniListView.as_view(), name='list_alumni'),
    path('alumni/<int:pk>/', AlumniDetailView.as_view(), name='detail_alumni'),
    path('alumni/tambah/', AlumniCreateView.as_view(), name='add_alumni'),
    path('alumni/<int:pk>/edit/', AlumniUpdateView.as_view(), name='edit_alumni'),
    path('alumni/<int:pk>/hapus/', AlumniDeleteView.as_view(), name='delete_alumni'),
]
