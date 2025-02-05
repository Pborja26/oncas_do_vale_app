from django.db import models, transaction
from django.core.exceptions import ValidationError
from utils.models import InfoModel
from user import models as user_models
# Create your models here.

class Balance(InfoModel):
  name = models.CharField(max_length=100, null=False, blank=False, unique=True)
  description = models.CharField(max_length=250, null=False, blank=False)
  value = models.DecimalField(decimal_places=2, max_digits=20, null=False, blank=False)

  def __str__(self):
    return str(self.name)
  
class FlowType(InfoModel):
  FLOW_TYPE_OPTIONS = [
    ("OUT", "Out"),
    ("IN", "In")
  ]

  name = models.CharField(max_length=50, null=False, blank=False, unique=True)
  flow_type = models.CharField(choices=FLOW_TYPE_OPTIONS, max_length=10, null=False, blank=False)

  def __str__(self):
    return str(self.name)
  
class CashFlow(InfoModel):
  user = models.ForeignKey(user_models.User, on_delete=models.PROTECT)
  flow_type = models.ForeignKey(FlowType, on_delete=models.PROTECT)
  value = models.DecimalField(decimal_places=2, max_digits=20, null=False, blank=False)
  balance = models.ForeignKey(Balance, on_delete=models.PROTECT)

  def save(self, *args, **kwargs):
    with transaction.atomic():
      balance = Balance.objects.select_for_update().get(id=self.balance.pk)

      if self.flow_type.flow_type == "IN":
        balance.value += self.value
      elif self.flow_type.flow_type == "OUT":
        if balance.value < self.value:
          raise ValidationError("Insuficient funds for transaction")
        balance.value -= self.value

      balance.save()
    super().save(*args, **kwargs)
