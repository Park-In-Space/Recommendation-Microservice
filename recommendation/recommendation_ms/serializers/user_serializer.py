from rest_framework import serializers

from recommendation_ms.models.user_model import User

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'