# main/views.py
import os
from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.conf import settings
from .models import FilesAdmin

def home(request):
    context = {'files': FilesAdmin.objects.all()}
    return render(request, 'myapp/home.html', context)

def download(request, file_path):
    file_path = os.path.join(settings.MEDIA_ROOT, file_path)
    if os.path.exists(file_path):
        with open(file_path, "rb") as fh:
            response = HttpResponse(fh.read(), content_type="application/pdf")
            response['Content-Disposition'] = 'inline;filename=' + os.path.basename(file_path)
            return response
    raise Http404
