from django.shortcuts import render
from rest_framework import viewsets
from Material import models as materialmodels
from Material import serializers as materialserializers
# Create your views here.

class ConditionViewSet(viewsets.ModelViewSet):
  queryset = materialmodels.Condition.objects.all()
  serializer_class = materialserializers.ConditionSerializer

class MaterialTypeViewSet(viewsets.ModelViewSet):
  queryset = materialmodels.MaterialType.objects.all()
  serializer_class = materialserializers.MaterialTypeSerializer

class MaterialViewSet(viewsets.ModelViewSet):
  queryset = materialmodels.Material.objects.all()
  serializer_class = materialserializers.MaterialSerializer

class ProductViewSet(viewsets.ModelViewSet):
  queryset = materialmodels.Product.objects.all()
  serializer_class = materialserializers.ProductSerializer
