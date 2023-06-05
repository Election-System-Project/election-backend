from django.db import models

# Create your models here.
class Candidate(models.Model):
    student_id = models.CharField(max_length = 9)
    name = models.CharField(max_length = 255, default = "a")
    surname = models.CharField(max_length = 255, default = "a")
    faculty = models.CharField(max_length = 255)
    department = models.CharField(max_length= 255)
    email = models.EmailField()
    grade = models.FloatField(default= 0.00)
    is_approved = models.BooleanField(default=False)
    vote_count = models.IntegerField(default = 0)
    is_winner = models.BooleanField(default=False)
    has_most_counts = models.BooleanField(default=False)