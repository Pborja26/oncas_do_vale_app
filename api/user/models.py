from django.db import models
from django.contrib.auth.models import AbstractUser, Permission
from django.contrib.auth.hashers import make_password, check_password
from utils.models import TimeStampedModel, InfoModel
# Create your models here.
class Group(InfoModel):
  name = models.CharField(max_length=50, null=False, blank=False, unique=True)
  description = models.CharField(max_length=250, null=False, blank=False)
  permissions = models.ManyToManyField(Permission, blank=True, related_name="group_permissions")

  def __str__(self):
    return str(self.name)
  
class User(AbstractUser, TimeStampedModel):
  name = models.CharField(max_length=250, null=False, blank=False)
  username = models.CharField(max_length=50, null=False, blank=False, unique=True)
  password = models.CharField(max_length=50, null=False, blank=False)
  email = models.EmailField(null=False, blank=False, unique=True)
  birth_date = models.DateField(null=False, blank=False)
  group = models.ForeignKey(Group, on_delete=models.SET_DEFAULT, default=1, null=False, blank=False)

  USERNAME_FIELD = "username"
  REQUIRED_FIELDS = ["name", "email", "birth_date"]

  def __str__(self):
    return str(self.name)
  
  def set_password(self, raw_password):
    self.password = make_password(raw_password)

  def check_password(self, raw_password):
    return check_password(raw_password, self.password)
  
class Athlete(InfoModel):
  CATEGORY_OPTIONS = [
    ("Female", "Female"),
    ("Male", "Male")
  ]

  user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
  nickname = models.CharField(max_length=50, null=True, blank=True)
  category = models.CharField(choices=CATEGORY_OPTIONS, max_length=12, null=False, blank=False)
  id_document = models.CharField(max_length=30, null=False, blank=False, unique=True)


  def __str__(self):
    return str(self.user)
