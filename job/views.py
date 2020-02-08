from job.serializers import JobDetailSerializer, JobListSerializer
from rest_framework import generics
from job.models import Job
from job.permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated

class JobCreateView(generics.CreateAPIView):
    serializer_class = JobDetailSerializer
    permission_classes = (IsAuthenticated, )


class JobListView(generics.ListAPIView):
    serializer_class = JobListSerializer
    queryset = Job.objects.all()


class JobDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = JobDetailSerializer
    queryset = Job.objects.all()
    permission_classes = (IsOwnerOrReadOnly, )
