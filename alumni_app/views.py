from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render
from .models import Alumni
from .forms import AlumniForm

# Home View
def home(request):
    return render(request, 'alumni_management/home.html')

# List Alumni (Menampilkan daftar alumni)
class AlumniListView(ListView):
    model = Alumni
    template_name = "alumni_management/list_alumni.html"
    context_object_name = "alumni_list"

# Detail Alumni (Menampilkan detail data alumni)
class AlumniDetailView(DetailView):
    model = Alumni
    template_name = "alumni_management/detail_alumni.html"
    context_object_name = "alumni"

# Create Alumni (Tambah data alumni)
class AlumniCreateView(CreateView):
    model = Alumni
    form_class = AlumniForm
    template_name = "alumni_management/add_alumni.html"
    success_url = reverse_lazy('list_alumni')

# Update Alumni (Edit data alumni)
class AlumniUpdateView(UpdateView):
    model = Alumni
    form_class = AlumniForm
    template_name = "alumni_management/edit_alumni.html"
    success_url = reverse_lazy('list_alumni')

# Delete Alumni (Hapus data alumni)
class AlumniDeleteView(DeleteView):
    model = Alumni
    template_name = "alumni_management/delete_alumni.html"
    success_url = reverse_lazy('list_alumni')
