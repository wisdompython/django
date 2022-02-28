from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    Title = models.CharField(max_length=100)
    Description = models.TextField()
    Date_Created = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    complete = models.BooleanField(default=False)
    def __str__(self):
        return self.Title

