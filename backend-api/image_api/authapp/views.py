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
def face(request):
    if request.method == 'POST':
        img_data = request.POST["face"].decode("base64")

        # Some method for face authenticate
        bool = 'Success'
   
    return render(request, 'authapp/auth.html', {'success': bool})
