from django.db import models
from django.contrib.auth.hashers import make_password, check_password
# Create your models here.
class Group(models.Model):
    name = models.CharField(max_length=30, null=False, blank=False)
    description = models.CharField(max_length=255, null=False, blank=False)
    created_in = models.DateTimeField(auto_now_add=True)
    updated_in = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)
    
class User(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    username = models.CharField(max_length=30, null=False, blank=False, unique=True)
    password = models.CharField(max_length=30, null=False, blank=False)
    group = models.ForeignKey(Group, on_delete=models.SET_DEFAULT, default=1)
    email = models.EmailField(null=False, blank=False, unique=True)
    created_in = models.DateTimeField(auto_now_add=True)
    updated_in = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)
    
    def set_password(self, raw_password):
        self.password = make_password(raw_password)
    
    def check_password(self, raw_password):
        return check_password(raw_password, self.password)
    
class Athlete(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=20, choices=[('M', 'Male'), ('F', 'Female')])
    id_document = models.CharField(max_length=20, null=False, blank=False)
    birth_date = models.DateField(null=False, blank=False)
    blood_type = models.CharField(max_length=5, choices=[('A+', 'A+'), ('B+', 'B+'), ('O+', 'O+'), ('AB+', 'AB+'), ('A-', 'A-'), ('B-', 'B-'), ('O-', 'O-'), ('AB-', 'AB-')], null=True)
    created_in = models.DateTimeField(auto_now_add=True)
    updated_in = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user)
