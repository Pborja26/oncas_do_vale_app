from rest_framework import serializers
from Material import models as materialmodels

class ConditionSerializer(serializers.ModelSerializer):
  class Meta:
    model = materialmodels.Condition
    fields = '__all__'

class MaterialTypeSerializer(serializers.ModelSerializer):
  class Meta:
    model = materialmodels.MaterialType
    fields = '__all__'

class MaterialSerializer(serializers.ModelSerializer):
  class Meta:
    model = materialmodels.Material
    fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
  class Meta:
    model = materialmodels.Product
    fields = '__all__'