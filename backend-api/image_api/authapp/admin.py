from django.contrib import admin
from .models import *

@admin.register(FaceImage)
class FaceImage(admin.ModelAdmin):
    pass


