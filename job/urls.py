from django.contrib import admin
from django.urls import path, include
from job.views import JobCreateView, JobListView, JobDetailView


app_name = 'job'

urlpatterns = [
    path('job/create/', JobCreateView.as_view()),
    path('all/', JobListView.as_view()),
    path('job/detail/<int:pk>/', JobDetailView.as_view()),
]
