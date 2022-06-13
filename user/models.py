from django.db import models
from django.contrib.auth.models import AbstractUser    

# Create your models here.

class CustomUser(AbstractUser):
    custom = models.CharField(max_length=1024, default='')
    phone = models.CharField(max_length=64, default='')
    adress = models.CharField(max_length=256, default='')
