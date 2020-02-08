from django.shortcuts import render
from job.serializers import JobCreateSerializer
from rest_framework import generics

class JobCreateView(generics.CreateAPIView):
    serializer_class = JobCreateSerializer
