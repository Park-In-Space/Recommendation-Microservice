from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Parking_lot(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    rating = models.PositiveIntegerField(
        default = 0,
        validators = [
            MaxValueValidator(5),
            MinValueValidator(0)
        ]
    )
    location = models.CharField(max_length=200)
    pricePerMinute = models.PositiveIntegerField()
    timeOpen = models.TimeField()
    timeClose = models.TimeField()
    

    class Meta:
        app_label = 'recommendation_ms'
