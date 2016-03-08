from django.db import models
from django.utils import timezone

# Create your models here.


class Congress(models.Model):
    title = models.CharField(max_length=200)
    place = models.CharField(max_length=200)
    description = models.TextField(default="", blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    start_date = models.DateField(null=True, default=timezone.now)
    end_date = models.DateField(null=True, default=timezone.now)

    longitude = models.FloatField(null=True)
    latitude = models.FloatField(null=True)

    def publish(self):
        self.save()

    def __str__(self):
        return self.title
