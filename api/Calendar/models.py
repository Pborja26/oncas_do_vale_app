from django.db import models
from User.models import Group, User
from Utils.models import TimestampedModel
# Create your models here.
class EventType(TimestampedModel):
  name = models.CharField(max_length=50, blank=False, null=False, unique=True)
  description = models.CharField(max_length=255)
  price = models.DecimalField(max_digits=10, decimal_places=2, default=00.00)

  def __str__(self):
    return str(self.name)

class Event(TimestampedModel):
  FREQUENCY_CHOICES = [
    ('daily', 'Daily'),
    ('weekly', 'Weekly'),
    ('monthly', 'Monthly'),
    ('quarterly', 'Quarterly'),
    ('yearly', 'Yearly'),
  ]
  event = models.ForeignKey(EventType, on_delete=models.CASCADE, null=False, blank=False)
  init_date = models.DateField(null=False, blank=False)
  start_time = models.TimeField(null=False, blank=False)
  end_date = models.DateField(null=True, blank=True)
  end_time = models.TimeField(null=True, blank=True)
  visibility = models.ManyToManyField(Group, related_name='Events')
  is_recurring = models.BooleanField(default=False)
  frequency = models.CharField(max_length=30, choices=FREQUENCY_CHOICES, null=True, blank=True)
  repeat_until = models.DateField(null=True, blank=True)

  def __str__(self):
    return str(self.event.name)

class EventPresence(TimestampedModel):
  event = models.ForeignKey(Event, on_delete=models.CASCADE)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  presence_confirmation = models.BooleanField()
  