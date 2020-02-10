from django.db import models

# Create your models here.

class PersonelInfo(models.Model):
    name = models.CharField(max_length=30)
    appoinment = models.CharField(max_length=30)
    joining_date = models.DateField()

class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=100, default=29.99)
    slug = models.SlugField()
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.title