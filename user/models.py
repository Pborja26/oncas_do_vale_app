import re
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password, check_password
from utils.models import TimeStampedModel, BaseInfoModel
# Create your models here.
class Group(BaseInfoModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, unique=True, null=False, blank=False)
    description = models.TextField(max_length=300, blank=True, null=True)

    def __str__(self):
        return str(self.name)

class User(AbstractUser, TimeStampedModel):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50, unique=True, blank=False, null=False)
    password = models.CharField(max_length=50, null=False, blank=False)
    name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(unique=True, null=False, blank=False)
    birth_date = models.DateField(null=True, blank=True)
    photo = models.FileField(upload_to="./" ,blank=True, null=True)
    group = models.ForeignKey(Group, on_delete=models.PROTECT, default=1)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["name", "email"]

    def __str__(self):
        return str(self.name)

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

class Athlete(BaseInfoModel):
    category_choices = [
        ("FEMALE", "Female"),
        ("MALE", "Male")
    ]
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cpf = models.CharField(max_length=14)
    rg = models.CharField(max_length=13)
    phone_number = models.CharField(max_length=14)
    category = models.CharField(choices=category_choices, blank=False, null=False)

    def format_cpf(self, cpf):
        digits = re.sub(r'\D', '', cpf)
        if len(digits) != 11:
            return cpf  # Deixa como está se não tiver 11 dígitos
        return f"{digits[:3]}.{digits[3:6]}.{digits[6:9]}-{digits[9:]}"

    def save(self, *args, **kwargs):
        if self.cpf:
            self.cpf = self.format_cpf(self.cpf)
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.id)
