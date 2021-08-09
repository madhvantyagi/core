from django.http.response import HttpResponse, HttpResponseBase
from django.shortcuts import render
from .models import QuesIntType, QuesMcq
import json

# Create your views here.
def index_questions(request):
    return HttpResponse('Questions Index Page')