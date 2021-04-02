from django.db import models


class User(models.Model):

    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=20)
    location = models.CharField(max_length=200)
    destination = models.CharField(max_length=200)
    rangeOfSearch = models.PositiveIntegerField( default = 0 )

    class Meta:
        app_label = 'recommendation_ms'
