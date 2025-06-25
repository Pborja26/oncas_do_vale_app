from django.db import models
# Create your models here.
class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class BaseInfoModel(TimeStampedModel):
    created_by = models.ForeignKey("user.User", null=False, blank=False, on_delete=models.PROTECT, related_name="%(class)s_created_by")
    updated_by = models.ForeignKey("user.User", null=False, blank=False, on_delete=models.PROTECT, related_name="%(class)s_updated_by")

    def save(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        if user:
            if not self.pk:
                self.created_by = user
            self.updated_by = user
        super().save(*args, **kwargs)

    class Meta:
        abstract = True
