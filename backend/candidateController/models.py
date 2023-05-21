from django.db import models

# Create your models here.
class Candidate(models.Model):
    student_id = models.CharField(max_length = 9)
    faculty = models.CharField(max_length = 255)
    department = models.CharField(max_length= 255)
    email = models.EmailField()
    is_approved = models.BooleanField(default=False)