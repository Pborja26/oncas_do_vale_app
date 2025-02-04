from django.db import models
from utils.models import InfoModel
from user import models as user_models
# Create your models here.

class Balance(InfoModel):
  name = models.CharField(max_length=100, null=False, blank=False, unique=True)
  description = models.CharField(max_length=250, null=False, blank=False)
  value = models.DecimalField(decimal_places=2, null=False, blank=False)

  def __str__(self):
    return str(self.value)
  
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
  value = models.DecimalField(decimal_places=2, null=False, blank=False)
