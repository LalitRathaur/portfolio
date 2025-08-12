from django.shortcuts import render, redirect
from django.conf import settings
from .models import Document, Project
from .form import DocumentForm, ProjectForm
from django.http import HttpResponse
import os
from django.urls import reverse
PASSWORD = "mysecret"
def portfolio(request):
    documents = Document.objects.all()
    projects = Project.objects.all()

    # Always initialize forms
    form = DocumentForm()
    project_form = ProjectForm()
    if request.method == 'POST':
        password = request.POST.get("password")

        # Password check
        if password != PASSWORD:
            return HttpResponse("Password is incorrect you cant save it")
        if 'upload_document' in request.POST:
           form = DocumentForm(request.POST, request.FILES)
           if form.is_valid():
              form.save()
              return redirect(reverse('portpolio'))
           else:
               print(form.errors)

        elif 'add_project' in request.POST:
            project_form = ProjectForm(request.POST)
            if project_form.is_valid():
                project_form.save()
                return redirect(reverse('portpolio'))

    # Profile image check
    profile_filename = "your_photo.jpg"
    profile_path = os.path.join(settings.MEDIA_ROOT, profile_filename)
    if os.path.isfile(profile_path):
        profile_image_url = request.build_absolute_uri(settings.MEDIA_URL + profile_filename)
    else:
        profile_image_url = None

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
