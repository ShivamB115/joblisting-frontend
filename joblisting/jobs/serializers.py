from rest_framework import serializers
from .models import api_job

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = api_job
        fields = '__all__'
