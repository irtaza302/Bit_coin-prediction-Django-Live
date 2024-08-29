# live_prediction/models.py

from django.db import models

class Prediction(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    current_price = models.FloatField()
    next_minute_price = models.FloatField()  # Add this field

    def __str__(self):
        return f"Prediction at {self.timestamp}"