from django.db import models
from datetime import date
# Create your models here.

class Video(models.Model):
    title= models.CharField(max_length=512)
    created_at = models.DateField(default=date.today)
    description = models.CharField(max_length=1024)
    video_file = models.FileField(blank=True, null=True)

    def __str__(self):
        return self.title