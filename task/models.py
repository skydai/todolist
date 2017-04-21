from django.db import models
import  datetime

class Task(models.Model):

    title = models.CharField(max_length=80)

    completed = models.BooleanField(default=False)
