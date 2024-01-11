from django.db import models

# Create your models here.
class Books(models.Model):
    author = models.CharField(max_length = 255)
    title = models.CharField(max_length = 255)
    description = models.TextField()
