from django.db import models
from Utils.models import TimestampedModel

# Create your models here.
class themeType(TimestampedModel):
  name = models.CharField(max_length=250)
  description = models.CharField(max_length=250, null=True, blank=True)

  def __str__(self):
    return str(self.name)

class theme(TimestampedModel):
  name = models.CharField(max_length=250, null=False)
  color = models.CharField(max_length=250, null=False)
  theme_type = models.ForeignKey(themeType, on_delete=models.CASCADE)
