from rest_framework import serializers

from recommendation_ms.models.parking_lot_model import Parking_lot


class Parking_lotSerializer(serializers.ModelSerializer):

    class Meta:
        model = Parking_lot
        fields = '__all__'