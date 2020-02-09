from django.db import models

# Create your models here.

class PersonelInfo(models.Model):
    name = models.CharField(max_length=30)
    appoinment = models.CharField(max_length=30)
    joining_date = models.DateField()

