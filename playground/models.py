from django.db import models

# Create your models here.

class Members(models.Model):
    brandname = models.CharField(max_length=255)
    productname = models.CharField(max_length=255)