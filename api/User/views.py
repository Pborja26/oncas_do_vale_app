from django.shortcuts import render
from rest_framework import viewsets
from User import serializers as userserializers
from User import models as usermodels
# Create your views here.

class GroupViewSet(viewsets.ModelViewSet):
    queryset = usermodels.Group.objects.all()
    serializer_class = userserializers.GroupSerializer

class UserViewSet(viewsets.ModelViewSet):
  queryset = usermodels.User.objects.all()
  serializer_class = userserializers.UserSerializer

class AthleteViewSet(viewsets.ModelViewSet):
  queryset = usermodels.Athlete.objects.all()
  serializer_class = userserializers.AthleteSerializer
