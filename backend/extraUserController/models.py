from django.db import models

# Create your models here.
class User(models.Model):
    email = models.EmailField(default="a@std.iyte.edu.tr")
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    studentNumber = models.CharField(max_length=20)
    hasVoted = models.BooleanField(default= False)
    hasApplied = models.BooleanField(default= False)
    electionStatus = models.BooleanField(default = False)
    grade = models.FloatField(default = 2.00)
    
    