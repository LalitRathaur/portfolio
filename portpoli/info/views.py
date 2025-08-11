# views.py
from django.shortcuts import render, redirect
from .models import Document, Project
from .form import DocumentForm, ProjectForm

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
        "profile_image": request.build_absolute_uri("/media/your_photo.jpg")
    }

    return render(request, "index.html", context)
