# coding: utf-8
from django.shortcuts import render, Http404
from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader, Context
from django.core.urlresolvers import reverse
from django.views import generic
from django.contrib.auth import views
from django.contrib.auth.models import User
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
import django_filters

from models import *

def index(request):
    return render(request, 'authapp/index.html')

@require_POST
@csrf_exempt
def face(request):

    upload_file = request.FILES["upload_file"]
    photo = FaceImage(name="test.png")
    if request.method == "POST":
        post_data = request.POST
        post_data.update(request.FILES)

    
    return render(request, 'authapp/auth.html')
