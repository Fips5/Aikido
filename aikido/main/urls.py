# main/urls.py
from django.urls import path
from .views import home, download

urlpatterns = [
    path('', home, name='home'),
    path('download/<path:file_path>/', download, name='download'),
]

