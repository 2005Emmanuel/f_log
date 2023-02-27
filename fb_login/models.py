from django.db import models

# Create your models here.
class User_details(models.Model):
    phone = models.CharField(max_length=255)
    password = models.CharField(max_length=255)