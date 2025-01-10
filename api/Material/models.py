from django.db import models
from Utils.models import TimestampedModel
# Create your models here.
class Condition(TimestampedModel):
    name = models.CharField(max_length=50, null=False,blank=False, unique=True)
    code = models.CharField(max_length=2, null=False, blank=False, unique=True)
    description = models.CharField(max_length=255, null=False, blank=False)
    created_in = models.DateTimeField(auto_now_add=True)
    updated_in = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)

class MaterialType(TimestampedModel):
    name = models.CharField(max_length=30, null=False, blank=False, unique=True)
    description = models.CharField(max_length=255, null=False, blank=False)
    created_in = models.DateTimeField(auto_now_add=True)
    updated_in = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)
    
class Material(TimestampedModel):
    name = models.CharField(max_length=100, null=False,blank=False)
    description = models.CharField(max_length=255, null=False, blank=True)
    material_type = models.ForeignKey(MaterialType, on_delete=models.CASCADE)
    condition = models.ForeignKey(Condition, on_delete=models.SET_DEFAULT, default=None)
    purchase_price = models.DecimalField(max_digits=6, decimal_places=2)
    purchased_in = models.DateField(null=False, blank=False)

class Product(TimestampedModel):
    name = models.CharField(max_length=255, null=False, blank=False)
    description = models.CharField(max_length=255, null=False, blank=False)
    in_stock = models.IntegerField(null=False, blank=False, default=0)
    production_price = models.DecimalField(max_digits=6, decimal_places=2)
    profit_margin = models.DecimalField(max_digits=6, decimal_places=2, default=00.00)
    selling_price = models.DecimalField(max_digits=6, decimal_places=2)

    def get_selling_price(self, *args, **kwargs):
        self.selling_price = self.production_price + (self.profit_margin * (self.production_price / 100))
    