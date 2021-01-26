import datetime

from django.db import models
from django.utils import timezone


# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=20)
    stock = models.IntegerField()
    price = models.FloatField()
    image_url = models.CharField(max_length=2083)

    def __str__(self):
        return self.name


class Offer(models.Model):
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=255)
    discount = models.FloatField()
    pub_date = models.DateTimeField('date published')

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.code
