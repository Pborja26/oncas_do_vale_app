from django.db import models

# Create your models here.
class TimestampedModel(models.Model):
    """Model with timestamps."""

    created_in = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_in = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        abstract = True