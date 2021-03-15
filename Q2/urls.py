from django.urls import path

from . import views

urlpatterns = [
    path('', views.get_collection_frequency, name='get_collection_frequency'),
]
