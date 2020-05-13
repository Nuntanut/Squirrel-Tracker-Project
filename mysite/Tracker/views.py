from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Squirrel

def index(request):
    return HttpResponse('Hello, This is tracker index')

def map(request):

    coordinates = Squirrel.objects.all()

    return render(request, 'Tracker/map.html', {'coordinates': coordinates,})

def sightings(request):

    squirrels = Squirrel.objects.all()

    return render(request, 'Tracker/sightings.html', {'squirrels': squirrels})

def sighting_squirrel_detail(request, unique_squirrel_id):

    squirrels = get_object_or_404(Squirrel, pk = unique_squirrel_id)

    return render(request, 'Tracker/squirrel_detail.html', {'squirrels': squirrels})

def sightings_stats(request):
    
    qs = Squirrel.objects.all()
    df = qs.to_dataframe()
    
    total = len(df)

    latitude = df['latitude'].mean()
    longitude = df['longitude'].mean()

    pivot = dict()

    rows = ['shift','primary_fur_color','age']
    pv = df.pivot_table(values='unique_squirrel_id', index=rows, aggfunc = 'count')
    pivot['1'] = pv.to_html()

    context = {
        'pivot': pivot,
        'total': total,
        'latitude': latitude,
        'longitude': longitude,
    }

    return render(request, 'Tracker/stats.html', context)

