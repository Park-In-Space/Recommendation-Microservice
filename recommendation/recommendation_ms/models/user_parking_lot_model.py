from django.db import models
from .parking_lot_model import Parking_lot
from .user_model import User


class User_Parking_lot(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    parking_lot = models.ForeignKey(Parking_lot, on_delete=models.CASCADE)
    recommended = models.BooleanField()
    distance_to_destination = models.PositiveIntegerField(default=0)
    

    class Meta:
        app_label = 'recommendation_ms'