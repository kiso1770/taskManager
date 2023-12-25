from django.db import models
from user.models import User


class TaskStatus(models.Model):
    title = models.CharField(max_length=100)
    color = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True)
    status = models.ForeignKey(TaskStatus, on_delete=models.SET_NULL, null=True)
    author_id = models.ForeignKey(User, on_delete=models.CASCADE)
    published_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
