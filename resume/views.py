from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import FileResponse
from .models import Resume

# Create your views here.

from django.shortcuts import render

def download_resume_page(request):
    return render(request, 'resume/download.html')

def download_resume(request):
    resume = get_object_or_404(Resume)
    return FileResponse(resume.file.open(), as_attachment=True, filename=resume.file.name)
