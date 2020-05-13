from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('list/', views.list_pets),
    path('<int:squirrel_id>/', views.get_squirrel),


    path('map/', views.map),
    path('sightings/', views.sightings),
    path('sightings/<str:unique_squirrel_id>/', views.sighting_squirrel_detail),
    path('sightings/stats/', views.sightings_stats),
]
