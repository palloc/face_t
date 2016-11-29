# coding:utf-8
from __future__ import unicode_literals
from django.db import models
from datetime import datetime

class FaceImage(models.Model):
    name = models.CharField(max_length=1024)
    image = models.ImageField(upload_to='images', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name
    
