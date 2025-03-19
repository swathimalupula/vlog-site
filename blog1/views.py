from django.shortcuts import render
from .models import Vlog, Photo  # Correct import path

def home(request):
    vlogs = Vlog.objects.all().order_by('-created_at')
    photos = Photo.objects.all().order_by('-uploaded_at')
    return render(request, 'blog1/home.html', {'vlogs': vlogs, 'photos': photos})
