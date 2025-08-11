from django.db import models
class info(models.Model):
    person=models.CharField(max_length=20)
    email=models.CharField(max_length=20)
    password=models.CharField(max_length=20)

class Document(models.Model):
    title = models.CharField(max_length=255)
    uploaded_file = models.FileField(upload_to='uploads/')  # files will be stored in MEDIA_ROOT/uploads/
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    timeline = models.CharField(max_length=100)  # e.g., "Jan 2024 - Apr 2024"
    domain = models.CharField(max_length=100)    # e.g., "Web Development"
    skills = models.CharField(max_length=255)    # e.g., "Python, Django, React"

    def __str__(self):
        return self.name