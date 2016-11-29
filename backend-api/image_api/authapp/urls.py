# config: utf-8
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'faceimage', FaceImageViewSet)
