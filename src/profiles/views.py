from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponse

# Create your views here.
def profiles_home(request):
    return HttpResponse("<h3> Profiles Home Page </h3>")