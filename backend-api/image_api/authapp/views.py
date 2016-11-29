# coding: utf-8
from django.shortcuts import render
import django_filters
from rest_framework import viewsets, filters

from .models import *
from .serializer import *

class FaceImageViewSet(viewsets.ModelViewSet):
    queryset = FaceImage.objects.all()
    serializer_class = FaceImageSerializer


