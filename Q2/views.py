from django.http import JsonResponse
from django.shortcuts import render
from Q2.models import *


def get_collection_frequency(request):
    collection_frequencies = Collection.objects.values_list('collection_frequency', flat=True)
    return JsonResponse(list(collection_frequencies), safe=False)
