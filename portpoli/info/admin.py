from django.contrib import admin
from info.models import info,Document,Project
class infoadmin(admin.ModelAdmin):
    list_display=('person','email','password')
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('title', 'uploaded_file', 'uploaded_at')

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'timeline', 'domain', 'skills')
admin.site.register(Document, DocumentAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(info,infoadmin)
# Register your models here.
