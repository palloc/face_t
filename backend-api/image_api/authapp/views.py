# coding: utf-8
from django.shortcuts import render, Http404
from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader, Context
from django.core.urlresolvers import reverse
from django.views import generic
from django.contrib.auth import views
from django.contrib.auth.models import User
import django_filters

from models import *

def index(request):
    return render(request, 'authapp/index.html')

