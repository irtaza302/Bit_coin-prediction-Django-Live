# live_prediction/tasks.py

from background_task import background
import requests
import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np
from .models import Prediction
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@background(schedule=60)  # Run every minute
def fetch_and_predict():
    try:
        # Fetch the current Bitcoin price
        response = requests.get('https://api.coindesk.com/v1/bpi/currentprice/BTC.json')
        response.raise_for_status()  # Raise an HTTPError for bad responses
        data = response.json()
        bitcoin_price = float(data['bpi']['USD']['rate'].replace(',', ''))
        logger.info(f"Fetched current Bitcoin price: {bitcoin_price}")
    except requests.RequestException as e:
        logger.error(f"Error fetching Bitcoin price: {e}")
        return
    except (ValueError, KeyError) as e:
        logger.error(f"Error parsing Bitcoin price: {e}")
        return

    # Static historical data for demonstration purposes
    historical_data = {
        'labels': list(range(1, 13)),  # Representing minutes for simplicity
        'prices': [30000, 32000, 31000, 35000, 37000, 40000, 42000, 45000, 47000, 49000, 50000, 52000]
    }

    # Prepare data for prediction
    df = pd.DataFrame({
        'Minute': np.arange(1, 13),
        'Price': historical_data['prices']
    })

    # Train a simple linear regression model
    model = LinearRegression()
    model.fit(df[['Minute']], df['Price'])
    logger.info("Trained linear regression model")

    # Predict the next minute's price using a DataFrame to preserve feature names
    next_minute_df = pd.DataFrame({'Minute': [len(df) + 1]})
    next_minute_price = model.predict(next_minute_df)[0]
    logger.info(f"Predicted next minute's Bitcoin price: {next_minute_price}")

    # Save the prediction to the database
    Prediction.objects.create(current_price=bitcoin_price, next_minute_price=next_minute_price)
    logger.info("Saved prediction to the database")