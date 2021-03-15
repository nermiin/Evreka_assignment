import django.utils.timezone as tz
from django.db.models import F
from django.http import JsonResponse
from .models import *


def get_last_points(request):
    last_points = NavigationRecord.objects.filter(
        datetime__range=[tz.datetime.now() + tz.timedelta(hours=-48), tz.datetime.now()]).annotate(
        plate=F('vehicle__plate')).values()

    points = [{
        'latitude': row.get('latitude'), 'longitude': row.get('longitude'), 'vehicle_plate': row.get('plate'),
        'datetime': tz.datetime.strftime(row.get('datetime'), "%d.%m.%Y %H:%M:%S")
    } for row in last_points]

    return JsonResponse(data=points, safe=False, json_dumps_params={'indent': 1})
