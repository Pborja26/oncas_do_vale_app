from django.db import models

# Create your models here.
class TimeStampedModel(models.Model):
  created_in = models.DateTimeField(auto_now_add=True)
  updated_in = models.DateTimeField(auto_now=True)

  class Meta:
    abstract = True

class InfoModel(models.Model):
  created_in = models.DateTimeField(auto_now_add=True)
  created_by = models.ForeignKey('user.User', on_delete=models.PROTECT, related_name="%(class)s_created_by")
  updated_in = models.DateTimeField(auto_now=True)
  updated_by = models.ForeignKey('user.User', on_delete=models.PROTECT, related_name="%(class)s_updated_by")

  class Meta:
    abstract = True