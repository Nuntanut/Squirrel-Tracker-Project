from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('map/', views.map),
    path('sightings/', views.sightings),
    path('sightings/stats/', views.sightings_stats),
    path('sightings/<str:unique_squirrel_id>/', views.sighting_squirrel_detail),
]
