from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User

# Create your models here.

class Cities(models.Model):
    id = models.AutoField(primary_key=True, unique=True, blank=False)
    name = models.CharField( unique = False, blank = False,max_length=30)
    geography = models.CharField(max_length=10000)
    history = models.CharField(max_length=10000)
    culture = models.CharField(max_length=10000)
    language = models.CharField(max_length=10000)
    infrastructure = models.CharField(max_length=10000)
    tourist_spots = models.CharField(max_length=10000)
    # posted_by = models.ForeignKey(User, on_delete=models.CASCADE,blank=False)



