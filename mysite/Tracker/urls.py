from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('<int:squirrel_id>/', views.get_squirrel),
]
