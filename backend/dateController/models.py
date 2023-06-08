from django.db import models

# Create your models here.
class ElectionDate(models.Model):
    election_type = models.CharField(max_length=255)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
