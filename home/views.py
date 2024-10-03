from sqlite3 import Timestamp
from django.shortcuts import render
from home.models import *
from django.http import JsonResponse



def index(request):
    return render(request, 'index.html')

def get_data(request):
    latest_date = LocationUpdate.objects.latest('timestamp')
    return JsonResponse({
            "latitude"  :   latest_date.latitude,
            "timestamp" :   latest_date.timestamp,
            "longitude" :   latest_date.longitude,
                    })