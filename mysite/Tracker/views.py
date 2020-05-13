from django.shortcuts import render
from django.http import HttpResponse

from .models import Squirrel

def index(request):
    return HttpResponse('Hello, This is tracker index')

def map(request):
    # implement needed #
    response_text = 'map'
    length = len(Squirrel.objects.all())
    coordinates = Squirrel.objects.all()
    context = {'length': length, 'coordinates': coordinates,}
    return render(request, 'Tracker/map.html', context)





def sightings(request):
    squirrels = Squirrel.objects.all()
    length = len(squirrels)
    content = {
        'Tracker': squirrels,
    }

    return render(request, 'Tracker/sightings.html', content)

def add_sightings(request):
    # implement needed #
    return HttpResponse('Hello, this is add sightings views')

def sightings_stats(request):
    # implement needed #
    return HttpResponse('Hello, this is sightings stats views')









#############################################################################

def list_pets(request):
    squirrels = Squirrel.objects.all()
    
    return render(request, 'Tracker/list.html', {'squirrels': squirrels})

def get_squirrel(request, squirrel_id):

    squirrel = Squirrel.opjects.get(id=squirrel_id)

    return HttpResponse(f'Hello, This is {squirrel.unique_squirrel_id}')
# Create your views here.
