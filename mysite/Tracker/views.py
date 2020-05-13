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

    return render(request, 'Tracker/squirrel_detail.html', {'sightings': sightings})

def sightings_stats(request):
    df = Squirrel.objects.all()
    
    latitude = list(df.aggregate(Avg('latitude')).values())[0]
    longitude = list(df.aggregate(Avg('longitude')).values())[0]

    df_pv = dict()

    df = Squirrel.objects.exclude(primary_fur_color__isnull = True).exclude(primary_fur_color = '').exclude(age__isnull = True).exclude(age = '?').exclude(age = '')
    rows = ['primary_fur_color','age']
    pt = df.to_pivot_table(values='unique_squirrel_id', rows=rows, aggfunc = 'count')
    df_pv['1'] = pt.to_html()

    df = Squirrel.objects.exclude(location__isnull = True).exclude(location = '').exclude(primary_fur_color__isnull = True).exclude(primary_fur_color = '')
    rows = ['primary_fur_color']
    cols = ['location']
    pt2 = df.to_pivot_table(values='unique_squirrel_id', rows=rows, cols=cols, aggfunc = 'count')
    df_pv['2'] = pt2.to_html()

    df = Squirrel.objects.exclude(location__isnull = True).exclude(location = '').exclude(shift__isnull = True).exclude(shift = '')
    rows = ['location']
    cols = ['shift']
    pt3 = df.to_pivot_table(values='unique_squirrel_id', rows=rows, cols=cols, aggfunc = 'count')
    df_pv['3'] = pt3.to_html()

    context = {'df_pv': df_pv}

    context = {
        'df_pv': df_pv,
        'latitude': latitude,
        'longitude': longitude,
    }

    return render(request, 'sightings/stats.html', context)








#############################################################################

def list_pets(request):
    squirrels = Squirrel.objects.all()
    
    return render(request, 'Tracker/list.html', {'squirrels': squirrels})

def get_squirrel(request, squirrel_id):

    squirrel = Squirrel.opjects.get(id=squirrel_id)

    return HttpResponse(f'Hello, This is {squirrel.unique_squirrel_id}')
# Create your views here.
