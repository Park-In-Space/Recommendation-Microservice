from django.db import models


class User(models.Model):

    id = models.PositiveIntegerField(primary_key = True)
    location = models.CharField(max_length=200)
    destination = models.CharField(max_length=200)
    rangeOfSearch = models.PositiveIntegerField( default = 0 )

    class Meta:
        app_label = 'recommendation_ms'
