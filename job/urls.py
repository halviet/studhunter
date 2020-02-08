from django.contrib import admin
from django.urls import path, include
from job.views import JobCreateView


app_name = 'job'

urlpatterns = [
    path('job/create', JobCreateView.as_view())
]
