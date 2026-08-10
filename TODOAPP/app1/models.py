from django.db import models
from django.contrib.auth.models import User

class Todo(models.Model):
    user =models.ForeignKey(User,on_delete=models.CASCADE)
    task=models.CharField(max_length=200)
    PRIORITY_CHOICES = [
        ('LOW','low'),
        ('MED','medium'),
        ('HIGH','high')
        ]
    priority=models.CharField(max_length=4,choices=PRIORITY_CHOICES,default="LOW")
    due_date=models.DateTimeField()
    completed = models.BooleanField(default=False)
# Create your models here.
