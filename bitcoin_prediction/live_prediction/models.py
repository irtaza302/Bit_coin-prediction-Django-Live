from django.db import models

class Prediction(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    current_price = models.FloatField()
    next_hour_price = models.FloatField()