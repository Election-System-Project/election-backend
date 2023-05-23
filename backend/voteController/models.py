from django.db import models

# Create your models here.

class Vote(models.Model):
    candidate_name = models.CharField(max_length=255)
    count = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.candidate_name} - {self.count}"