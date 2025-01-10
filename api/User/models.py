from django.db import models
from django.contrib.auth.hashers import make_password, check_password
from Utils.models import TimestampedModel
# Create your models here.
class Group(TimestampedModel):
    name = models.CharField(max_length=30, null=False, blank=False)
    description = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return str(self.name)
    
class User(TimestampedModel):
    name = models.CharField(max_length=255, null=False, blank=False)
    username = models.CharField(max_length=30, null=False, blank=False, unique=True)
    password = models.CharField(max_length=30, null=False, blank=False)
    group = models.ForeignKey(Group, on_delete=models.SET_DEFAULT, default=1)
    email = models.EmailField(null=False, blank=False, unique=True)

    def __str__(self):
        return str(self.name)
    
    def set_password(self, raw_password):
        self.password = make_password(raw_password)
    
    def check_password(self, raw_password):
        return check_password(raw_password, self.password)
    
class Athlete(TimestampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=20, choices=[('M', 'Male'), ('F', 'Female')])
    id_document = models.CharField(max_length=20, null=False, blank=False)
    birth_date = models.DateField(null=False, blank=False)
    blood_type = models.CharField(max_length=5, choices=[('A+', 'A+'), ('B+', 'B+'), ('O+', 'O+'), ('AB+', 'AB+'), ('A-', 'A-'), ('B-', 'B-'), ('O-', 'O-'), ('AB-', 'AB-')], null=True)

    def __str__(self):
        return str(self.user)
