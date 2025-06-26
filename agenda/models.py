from django.db import models
from datetime import timedelta
from dateutil.relativedelta import relativedelta
from utils.models import BaseInfoModel

# Create your models here.
class Local(BaseInfoModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150, null=False, blank=False)
    contact = models.CharField(max_length=14, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    city = models.CharField(max_length=100, null=False, blank=False)
    address = models.CharField(max_length=250, null=False, blank=False)
    number = models.CharField(max_length=20, null=True, blank=True)
    complement = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return str(self.name)

class EventType(BaseInfoModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False, blank=False, unique=True)
    description = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return str(self.name)

class Event(BaseInfoModel):
    recurrency = [
        ("UNIQUE", "Unique"),
        ("DAILY", "Daily"),
        ("WEEKLY", "Weekly"),
        ("MONTHLY", "Monthly"),
        ("ANUALLY", "Anually"),
    ]

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    event_type = models.ForeignKey(EventType, on_delete=models.PROTECT)
    local = models.ForeignKey(Local, on_delete=models.PROTECT)
    date_init = models.DateField()
    date_end = models.DateField()
    time_init = models.TimeField()
    time_end = models.TimeField()
    is_recurrent = models.BooleanField(default=False)
    recurrency = models.CharField(max_length=10, choices=recurrency,  default="UNIQUE")
    repeat_until = models.DateField(null=True, blank=True)
    is_generated = models.BooleanField(default=False)

    def __str__(self):
        return str(self.name)
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.is_recurrent and not self.is_generated:
            delta = None
            if self.recurrency == "DAILY":
                delta = timedelta(days=1)
            elif self.recurrency == "WEEKLY":
                delta = timedelta(weeks=1)
            elif self.recurrency == "MONTHLY":
                delta = relativedelta(months=1)
            elif self.recurrency == "ANUALLY":
                delta = relativedelta(years=1)

            if delta is not None:
                current_date = self.date_init + delta
                while current_date <= self.repeat_until:
                    Event.objects.create(
                        name=self.name,
                        description=self.description,
                        event_type=self.event_type,
                        date_init=current_date,
                        date_end=self.date_end + delta,
                        time_init=self.time_init,
                        time_end=self.time_end,
                        is_recurrent=False,
                        recurrency="UNIQUE",
                        repeat_until=None,
                        is_generated=True,
                        created_by=self.created_by,
                        created_at=self.created_at,
                        updated_by=self.updated_by,
                        updated_at=self.updated_at
                    )
                    current_date += delta
