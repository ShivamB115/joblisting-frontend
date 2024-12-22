from rest_framework import viewsets
from .models import api_job
from .serializers import JobSerializer
from django.http import HttpResponse

class JobViewSet(viewsets.ModelViewSet):
    queryset = api_job.objects.all()
    serializer_class = JobSerializer

def index(request):
    return HttpResponse("Welcome to the Job Listings site!")
