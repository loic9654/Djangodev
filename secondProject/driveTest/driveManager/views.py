from django.shortcuts import render

from .models import Project, Observation

# Get Project and display them
def index(request):
    return render(request, 'projects/index.html')