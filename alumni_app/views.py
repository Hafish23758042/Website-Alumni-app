from django.shortcuts import render, redirect, get_object_or_404
from .models import Alumni
from .forms import AlumniForm

def home(request):
    return render(request, 'alumni_management/home.html')

# Create (Tambah data alumni)
def add_alumni(request):
    if request.method == "POST":
        form = AlumniForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_alumni')
    else:
        form = AlumniForm()
    return render(request, 'alumni_management/add_alumni.html', {'form': form})

# Read (Menampilkan daftar alumni)
def list_alumni(request):
    alumni_list = Alumni.objects.all()
    return render(request, 'alumni_management/list_alumni.html', {'alumni_list': alumni_list})

# Update (Edit data alumni)
def edit_alumni(request, id):
    alumni = get_object_or_404(Alumni, id=id)
    if request.method == "POST":
        form = AlumniForm(request.POST, instance=alumni)
        if form.is_valid():
            form.save()
            return redirect('list_alumni')
    else:
        form = AlumniForm(instance=alumni)
    return render(request, 'alumni_management/edit_alumni.html', {'form': form})

# Delete (Hapus data alumni)
def delete_alumni(request, id):
    alumni = get_object_or_404(Alumni, id=id)
    if request.method == "POST":
        alumni.delete()
        return redirect('list_alumni')
    return render(request, 'alumni_management/delete_alumni.html', {'alumni': alumni})
