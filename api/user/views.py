from django.shortcuts import render
from utils.views import BaseViewSet
from user import models as user_models
from user import serializers as user_serializers
from user import filtersets as user_filters
# Create your views here.

class GroupViewSet(BaseViewSet):
  queryset = user_models.Group.objects.all()
  filterset_class = user_filters.GroupFilterSet
  serializer_class = user_serializers.GroupSerializer

class UserViewSet(BaseViewSet):
  queryset = user_models.User.objects.all()
  filterset_class = user_filters.UserFilterSet
  serializer_class = user_serializers.UserSerializer

class AthleteViewSet(BaseViewSet):
  queryset = user_models.Athlete.objects.all()
  filterset_class = user_filters.AthleteFilterSet
  serializer_class = user_serializers.AthleteSerializer