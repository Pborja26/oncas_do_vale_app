from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from user import serializers as user_serializers
from user import models as user_models
# Create your views here.
class GroupViewSet(ModelViewSet):
    queryset = user_models.Group.objects.all()
    serializer_class = user_serializers.GroupSerializer

class UserViewSet(ModelViewSet):
    queryset = user_models.User.objects.all()
    serializer_class = user_serializers.UserSerializer
