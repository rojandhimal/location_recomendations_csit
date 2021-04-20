from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User


# Create your models here.

class Location(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    location_logo = models.FileField()
    description = models.TextField(null=True,blank=True)
    lalitude = models.CharField(max_length=50,null=True,blank=True)
    longitude = models.CharField(max_length=50,null=True,blank=True)

    def __str__(self):
        return self.title


class Myrating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0, validators=[MaxValueValidator(5), MinValueValidator(0)])

class MyList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    Visited = models.BooleanField(default=False)
