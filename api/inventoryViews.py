from django.shortcuts import render
from django.template.response import TemplateResponse
from django.http import HttpResponse,JsonResponse
from rest_framework.renderers import JSONRenderer
from django.contrib.auth.models import Group
import json
from inventory import models
from inventory import serializers




