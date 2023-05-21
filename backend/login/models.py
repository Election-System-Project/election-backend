from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=255)
    student_number = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=255)
    grade = models.CharField(max_length=10)
    email = models.EmailField(unique=True)
    auth_token = models.CharField(max_length=255, blank=True, null=True)
    expires_after = models.IntegerField(default=5)