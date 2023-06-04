from django.db import models

# Create your models here.


class Student(models.Model):
    student_id = models.IntegerField(primary_key=True)

class PDF(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    file = models.FileField(upload_to='pdfs/')
    student = models.ForeignKey(Student, on_delete=models.CASCADE)