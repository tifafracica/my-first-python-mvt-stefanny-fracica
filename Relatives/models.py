from django.db import models

# Create your models here.
class Relative(models.Model):

    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    age = models.IntegerField()
    birthday = models.DateField()

