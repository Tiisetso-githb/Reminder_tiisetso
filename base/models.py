# models.py
from django.db import models
from django.utils import timezone

class Reminder(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    due_date = models.DateField(default=timezone.now)  # Default to current date
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title



