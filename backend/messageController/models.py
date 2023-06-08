from django.db import models
from extraUserController.models import User

# Create your models here.
class Message(models.Model):
    content = models.TextField(default= ' ')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    