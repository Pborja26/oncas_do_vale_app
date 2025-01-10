from rest_framework import serializers
from Base import models as basemodels

class ThemeTypeSerializer(serializers.ModelSerializer):
  class Meta:
    model = basemodels.themeType
    fields = '__all__'

class ThemeSerializer(serializers.ModelSerializer):
  class Meta:
    model = basemodels.theme
    fields = '__all__'

