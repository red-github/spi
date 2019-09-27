from django.urls import path, include
from rest_framework import routers
from django.conf.urls import url
from fizzbuzz.views import FizzbuzzApiView



urlpatterns = (
    path('fizz-buzz/', FizzbuzzApiView.as_view(), name="User List"),
)
