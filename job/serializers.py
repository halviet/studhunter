from rest_framework import serializers
from job.models import Job

class JobCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'