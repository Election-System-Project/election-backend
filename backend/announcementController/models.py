from django.db import models

# Create your models here.
class Announcement(models.Model):
    title = models.CharField(max_length = 255)
    content = models.TextField()
    announcement_type = models.CharField(max_length = 255)
