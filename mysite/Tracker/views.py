from django.shortcuts import render
from django.http import HttpResponse

from .models import Squirrel

def index(request):
    return HttpResponse('Hello, This is tracker index')

def list_pets(request):
    squirrels = Squirrel.objects.all()
    
    return render(request, 'Tracker/list.html', {'squirrels': squirrels})

def get_squirrel(request, squirrel_id):

    squirrel = Squirrel.opjects.get(id=squirrel_id)

    return HttpResponse(f'Hello, This is {squirrel.unique_squirrel_id}')
# Create your views here.
