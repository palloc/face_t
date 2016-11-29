# coding: utf-8

from rest_framework import serializers
from .models import *

class FaceImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = FaceImage
        fields = ('name', 'image', 'created_at')
        
