# live_prediction/views.py

from django.shortcuts import render
from django.http import JsonResponse
from .models import Prediction

def index(request):
    latest_prediction = Prediction.objects.latest('timestamp')
    bitcoin_price = latest_prediction.current_price
    next_hour_price = latest_prediction.next_hour_price

    # Static historical data for demonstration purposes
    historical_data = {
        'labels': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
        'prices': [30000, 32000, 31000, 35000, 37000, 40000, 42000, 45000, 47000, 49000, 50000, 52000]
    }

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse({'bitcoin_price': bitcoin_price, 'next_hour_price': next_hour_price})

    return render(request, 'live_prediction/index.html', {
        'bitcoin_price': bitcoin_price,
        'historical_data': historical_data,
        'next_hour_price': next_hour_price
    })