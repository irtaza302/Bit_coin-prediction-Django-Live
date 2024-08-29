# live_prediction/views.py

from django.shortcuts import render
from django.http import JsonResponse
from .models import Prediction
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def index(request):
    try:
        # Fetch the latest prediction from the database
        latest_prediction = Prediction.objects.latest('timestamp')
        bitcoin_price = latest_prediction.current_price
        next_minute_price = latest_prediction.next_minute_price
        logger.info(f"Fetched latest prediction: current_price={bitcoin_price}, next_minute_price={next_minute_price}")
    except Prediction.DoesNotExist:
        logger.error("No predictions found in the database")
        bitcoin_price = None
        next_minute_price = None

    # Static historical data for demonstration purposes
    historical_data = {
        'labels': list(range(1, 13)),  # Representing minutes for simplicity
        'prices': [30000, 32000, 31000, 35000, 37000, 40000, 42000, 45000, 47000, 49000, 50000, 52000]
    }

    # Check if the request is an AJAX request
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse({'bitcoin_price': bitcoin_price, 'next_minute_price': next_minute_price})

    # Render the template with the fetched data
    return render(request, 'live_prediction/index.html', {
        'bitcoin_price': bitcoin_price,
        'historical_data': historical_data,
        'next_minute_price': next_minute_price
    })