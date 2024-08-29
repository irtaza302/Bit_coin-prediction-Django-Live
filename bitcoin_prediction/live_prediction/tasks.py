# live_prediction/tasks.py

from background_task import background
import requests
import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np
from .models import Prediction

@background(schedule=60)
def fetch_and_predict():
    # Fetch the current Bitcoin price
    response = requests.get('https://api.coindesk.com/v1/bpi/currentprice/BTC.json')
    data = response.json()
    bitcoin_price = float(data['bpi']['USD']['rate'].replace(',', ''))

    # Static historical data for demonstration purposes
    historical_data = {
        'labels': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
        'prices': [30000, 32000, 31000, 35000, 37000, 40000, 42000, 45000, 47000, 49000, 50000, 52000]
    }

    # Prepare data for prediction
    df = pd.DataFrame({
        'Month': np.arange(1, 13),
        'Price': historical_data['prices']
    })

    # Train a simple linear regression model
    model = LinearRegression()
    model.fit(df[['Month']], df['Price'])

    # Predict the next hour's price using a DataFrame to preserve feature names
    next_hour_df = pd.DataFrame({'Month': [len(df) + 1]})
    next_hour_price = model.predict(next_hour_df)[0]

    # Save the prediction to the database
    Prediction.objects.create(current_price=bitcoin_price, next_hour_price=next_hour_price)