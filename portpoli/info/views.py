# views.py
# views.py
from django.shortcuts import render, redirect
from django.conf import settings
from .models import Document, Project
from .form import DocumentForm, ProjectForm
import os

def portfolio(request):
    documents = Document.objects.all()
    projects = Project.objects.all()

    if request.method == 'POST':
        if 'upload_document' in request.POST:
            form = DocumentForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('portfolio')

        elif 'add_project' in request.POST:
            project_form = ProjectForm(request.POST)
            if project_form.is_valid():
                project_form.save()
                return redirect('portfolio')
    else:
        form = DocumentForm()
        project_form = ProjectForm()

    # Check if profile image exists in media
    profile_filename = "your_photo.jpg"  # name of your image file in MEDIA_ROOT
    profile_image_url = (
        request.build_absolute_uri(settings.MEDIA_URL + profile_filename)
        if os.path.exists(os.path.join(settings.MEDIA_ROOT, profile_filename))
        else None
    )

    context = {
        "name": "Lalit Rathaur",
        "role": "Software Developer / CS Student at IIT Indore",
        "branch": "Computer Science",
        "cpi": "7.51",
        "codeforces": "1911 (Candidate Master)",
        "leetcode": "2199",
        "codechef": "2177",
        "about": "I am passionate about problem-solving, competitive programming, and building full-stack applications.",
        "projects": projects,
        "documents": documents,
        "form": form,
        "project_form": project_form,
        "profile_image": profile_image_url
    }

    return render(request, "index.html", context)
