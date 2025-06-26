from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from user import serializers as user_serializers
from user import models as user_models
from user import fitersets as user_filters 
# Create your views here.
class GroupViewSet(ModelViewSet):
    queryset = user_models.Group.objects.all()
    filterset_class = user_filters.GroupFilterSet
    serializer_class = user_serializers.GroupSerializer

class UserViewSet(ModelViewSet):
    queryset = user_models.User.objects.all()
    filterset_class = user_filters.UserFilterSet
    serializer_class = user_serializers.UserSerializer

class AthleteViewSet(ModelViewSet):
    queryset = user_models.Athlete.objects.all()
    filterset_class = user_filters.AthleteFilterSet
    serializer_class = user_serializers.AthleteSerializer
