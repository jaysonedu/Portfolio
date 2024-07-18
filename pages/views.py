from django.shortcuts import render
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from .models import HomePageContent

def home(request):
    home_content = HomePageContent.objects.first()  # Assuming there's only one record
    return render(request, 'pages/home.html', {'home_content': home_content})


