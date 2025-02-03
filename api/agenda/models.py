from django.db import models
from utils.models import InfoModel
from user import models as user_models
from datetime import datetime, timedelta
# Create your models here.

class EventType(InfoModel):
  name = models.CharField(max_length=50, null=False, blank=False, unique=True)
  description = models.CharField(max_length=250, null=False,blank=False)

  def __str__(self):
    return str(self.name)
  
class Event(InfoModel):
  RECURRENCI_OPTIONS = [
    ("Unique", "Unique"),
    ("Daily", "Daily"),
    ("Weekly", "Weekly"),
    ("Monthly", "Monthly")
  ]

  name = models.CharField(max_length=150, null=False, blank=False)
  description = models.CharField(max_length=250, null=False, blank=False)
  event_type = models.ForeignKey(EventType, on_delete=models.CASCADE, null=False, blank=False)
  visibility = models.ForeignKey(user_models.Group, on_delete=models.CASCADE, null=False, blank=False)
  init_date = models.DateField(null=False, blank=False)
  init_time = models.TimeField(null=False, blank=False)
  end_date = models.DateField(null=True, blank=True)
  end_time = models.TimeField(null=True, blank=True)
  recurrenci = models.CharField(choices=RECURRENCI_OPTIONS, max_length=50, null=True, blank=True)
  repeat_until = models.DateField(null=True, blank=True)

  def __str__(self):
     return str(self.id)

  def save(self, *args, **kwargs):
    is_new = self.pk is None  # Verifica se o evento está sendo criado agora
    super().save(*args, **kwargs)  # Salva o evento original primeiro

    # Se for um evento recorrente e a data limite for válida
    if is_new and self.recurrenci and self.recurrenci != "Unique" and self.repeat_until:
        current_date = self.init_date

        # Criando eventos recorrentes até a data limite
        while current_date < self.repeat_until:  # Evita criar eventos na mesma data
            if self.recurrenci == "Daily":
                current_date += timedelta(days=1)
            elif self.recurrenci == "Weekly":
                current_date += timedelta(weeks=1)
            elif self.recurrenci == "Monthly":
                current_date = (current_date.replace(day=1) + timedelta(days=32)).replace(day=self.init_date.day)

            # Evita criar um evento após o limite
            if current_date > self.repeat_until:
                break

            Event.objects.create(
                name=self.name,
                description=self.description,
                event_type=self.event_type,
                visibility=self.visibility,
                init_date=current_date,
                init_time=self.init_time,
                end_date=self.end_date,
                end_time=self.end_time,
                recurrenci="Unique",
                repeat_until=None,
                created_by=self.created_by,
                updated_by=self.updated_by
            )

  

class EventPresence(InfoModel):
   event_id = models.ForeignKey(Event, on_delete=models.PROTECT)
   user = models.ForeignKey(user_models.User, on_delete=models.PROTECT)
