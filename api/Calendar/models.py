from django.db import models
from User.models import Group, User
from datetime import date, timedelta
# Create your models here.
class EventType(models.Model):
  name = models.CharField(max_length=50, blank=False, null=False, unique=True)
  description = models.CharField(max_length=255)
  created_in = models.DateTimeField(auto_now_add=True)
  updated_in = models.DateTimeField(auto_now=True)

  def __str__(self):
    return str(self.name)

class Event(models.Model):
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
  
  def generate_recurring_events(self):
        """
        Gera eventos recorrentes com base na frequência e na data final.
        """
        if not self.is_recurring or not self.frequency or not self.repeat_until:
            return []

        occurrences = []
        current_date = self.init_date

        while current_date <= self.repeat_until:
            occurrences.append(current_date)

            # Incrementa a data com base na frequência
            if self.frequency == 'daily':
                current_date += timedelta(days=1)
            elif self.frequency == 'weekly':
                current_date += timedelta(weeks=1)
            elif self.frequency == 'monthly':
                # Adiciona um mês, respeitando limites de dias no mês
                month = current_date.month + 1 if current_date.month < 12 else 1
                year = current_date.year if current_date.month < 12 else current_date.year + 1
                day = min(current_date.day, (date(year, month + 1, 1) - timedelta(days=1)).day)
                current_date = current_date.replace(year=year, month=month, day=day)
            elif self.frequency == 'yearly':
                # Incrementa um ano
                current_date = current_date.replace(year=current_date.year + 1)

        return occurrences


class EventPresence(models.Model):
  event = models.ForeignKey(Event, on_delete=models.CASCADE)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  presence_confirmation = models.BooleanField()
  