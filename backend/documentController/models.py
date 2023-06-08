from django.db import models
from candidateController.models import Candidate
from extraUserController.models import User

# Create your models here.
class PDF(models.Model):
    file = models.FileField(upload_to='pdfs/')
    student = models.ForeignKey(Candidate, on_delete=models.CASCADE)