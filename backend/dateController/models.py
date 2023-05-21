from django.db import models

# Create your models here.
class ElectionDate(models.Model):
    election_type = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
