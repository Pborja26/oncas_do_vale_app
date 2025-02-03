from rest_framework import serializers
from user import models as user_models
from datetime import date

class GroupSerializer(serializers.ModelSerializer):
  class Meta:
    model = user_models.Group
    fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
  age = serializers.SerializerMethodField()

  class Meta:
    model = user_models.User
    fields = [
        "id",
        "name",
        "username",
        "email",
        "birth_date",
        "group",
        "age"
      ]

  def get_age(self,obj):
    today = date.today()

    age = today.year - obj.birth_date.year
    if today.month < obj.birth_date.month or (today.month == obj.birth_date.month and 
      today.day < obj.birth_date.day):
      age -= 1
    
    return age
  
class AthleteSerializer(serializers.ModelSerializer):
  class Meta:
    model = user_models.Athlete
    fields = "__all__"