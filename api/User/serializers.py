from rest_framework import serializers
from User import models as usermodels

class GroupSerializer(serializers.ModelSerializer):
  class Meta:
    model = usermodels.Group
    fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = usermodels.User
    fields = '__all__'

class AthleteSerializer(serializers.ModelSerializer):
  class Meta:
    model = usermodels.Athlete
    fields = '__all__'