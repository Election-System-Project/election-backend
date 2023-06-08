from django.db import models

# Create your models here.
class Candidate(models.Model):
    student_id = models.CharField(max_length = 9, primary_key=True)
    name = models.CharField(max_length = 255, default = "a")
    surname = models.CharField(max_length = 255, default = "a")
    department = models.CharField(max_length= 255)
    email = models.EmailField()
    grade = models.FloatField(default= 0.00)
    is_approved = models.BooleanField(default=False)
    vote_count = models.IntegerField(default = 0)
    is_winner = models.BooleanField(default=False)
    has_most_counts = models.BooleanField(default=False)
    is_checked = models.BooleanField(default=False)

    def __str__(self):
        return self.student_id + " " + self.name + " "+ self.surname