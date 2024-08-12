# personal_portfolio/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("resume/", include('resume.urls')),
    path("admin/", admin.site.urls),
    path("", include("pages.urls")),
    path("projects/", include("projects.urls")),
    path("", include("sendemail.urls")),
    path("NotImplemented/", include("NotImplemented.urls"),)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)