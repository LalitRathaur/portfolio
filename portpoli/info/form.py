# app/forms.py
from django import forms
from .models import Document,Project

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['title', 'uploaded_file']

class ProjectForm(forms.ModelForm):
    skills = forms.CharField(
        help_text="Enter skills separated by commas"
    )

    class Meta:
        model = Project
        fields = ['name', 'description', 'domain', 'timeline', 'skills']

    def clean_skills(self):
        skills_str = self.cleaned_data['skills']
        return [skill.strip() for skill in skills_str.split(',') if skill.strip()]