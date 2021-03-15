from django.urls import path

from . import views

urlpatterns = [
    path('', views.get_last_points, name='get_last_points'),
]
