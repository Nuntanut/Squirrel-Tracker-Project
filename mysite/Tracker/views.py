from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello, This is tracker index')
# Create your views here.
