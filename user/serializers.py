from rest_framework import serializers
from user import models as user_models

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = user_models.Group
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    group = GroupSerializer()

    class Meta:
        model = user_models.User
        fields = ["id", "name", "username", "group"]

class AthleteSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = user_models.Athlete
        fields = ["id", "user", "category"]