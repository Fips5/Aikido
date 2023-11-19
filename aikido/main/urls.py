# main/urls.py
from . import views
from django.urls import path
from . import views

urlpatterns = [
    # Add the URL pattern for the home view here
    path('', views.home, name='home'),
]
