from django.db import models

# Create your models here.


class Members(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
