from rest_framework import serializers

from recommendation_ms.models.user_parking_lot_model import User_Parking_lot

class User_Parking_lotSerializer(serializers.ModelSerializer):

    class Meta:
        model = User_Parking_lot
        fields = '__all__'