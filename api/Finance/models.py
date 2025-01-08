from django.db import models

# Create your models here.
class FlowType(models.Model):
  name = models.CharField(max_length=50, null=False, blank=False, unique=True)
  description = models.CharField(max_length=255, null=False, blank=False)
  category = models.CharField(max_length=7, choices=[('entrada', 'Entrada'), ('saida', 'Saída')])
  created_in = models.DateTimeField(auto_now_add=True)
  updated_in = models.DateTimeField(auto_now=True)

  def __str__(self):
    return str(self.name)
  
class Balance(models.Model):
  balance = models.DecimalField(max_digits=10, decimal_places=2)
  created_in = models.DateTimeField(auto_now_add=True)
  updated_in = models.DateTimeField(auto_now=True)

class CashFlow(models.Model):
  flow_type = models.ForeignKey(FlowType, on_delete=models.CASCADE)
  value = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
  mov_date = models.DateTimeField(auto_now_add=True)
  balance = models.ForeignKey(Balance, on_delete=models.CASCADE)

  def save(self, *args, **kwargs):
    if not self.pk:
      if self.flow_type.category == 'entrada':
        self.balance.balance += self.value
      elif self.flow_type.category == 'saida':
        self.balance.balance -= self.value
      self.balance.save()
    super().save(*args, **kwargs)