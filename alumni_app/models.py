from django.db import models

class Alumni(models.Model):
 name = models.CharField(max_length=100)
 email = models.EmailField(unique=True)
 graduation_year = models.IntegerField()
 major = models.CharField(max_length=100)
 job_position = models.CharField(max_length=100)
 company = models.CharField(max_length=100)