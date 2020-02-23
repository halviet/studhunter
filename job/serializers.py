from rest_framework import serializers
from job.models import Job

class JobDetailSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Job
        fields = '__all__'

class JobListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'