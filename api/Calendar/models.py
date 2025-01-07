from django.db import models
from User.models import Group, User
# Create your models here.
class EventType(models.Model):
  name = models.CharField(max_length=50, blank=False, null=False, unique=True)
  description = models.CharField(max_length=255)
  created_in = models.DateTimeField(auto_now_add=True)
  updated_in = models.DateTimeField(auto_now=True)

  def __str__(self):
    return str(self.name)

class Event(models.Model):
  event = models.ForeignKey(EventType, on_delete=models.CASCADE, null=False, blank=False)
  init_date = models.DateField(null=False, blank=False)
  start_time = models.TimeField(null=False, blank=False)
  end_date = models.DateField()
  end_time = models.TimeField()
  visibility = models.ManyToManyField(Group, related_name='Events')
  send_invite = models.BooleanField(null=False, blank=False)
  invite_date = models.DateTimeField()
  send_reminder = models.BooleanField(null=False, blank=False)
  reminder_date = models.DateTimeField()

class EventPresence(models.Model):
  event = models.ForeignKey(Event, on_delete=models.CASCADE)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  presence_confirmation = models.BooleanField()
  