from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=100)
    track = models.CharField(max_length=100)
    hours = models.DecimalField(max_digits=5, decimal_places=2)