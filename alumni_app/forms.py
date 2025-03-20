from django import forms
from .models import Alumni

class AlumniForm(forms.ModelForm):
    class Meta:
        model = Alumni
        fields = ['name', 'email', 'graduation_year', 'major', 'job_position', 'company']
