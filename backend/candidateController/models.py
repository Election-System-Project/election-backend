from django.db import models

# Create your models here.
class Candidate(models.Model):
    student_id = models.CharField(max_length = 9)
    name = models.CharField(max_length = 255, default = "a")
    surname = models.CharField(max_length = 255, default = "a")
    faculty = models.CharField(max_length = 255)
    department = models.CharField(max_length= 255)
    email = models.EmailField()
    grade = models.IntegerField(default = 1)
    is_approved = models.BooleanField(default=False)