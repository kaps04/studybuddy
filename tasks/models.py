from django.db import models
from django.conf import settings


class Task(models.Model):
    PRIORITY_CHOICES = [
        ("Low", "Low"),
        ("Medium", "Medium"),
        ("High", "High"),
    ]

    # NEW: Connect each task to its user
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="tasks",
    )

    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

    priority = models.CharField(
        max_length=20,
        choices=PRIORITY_CHOICES,
        default="Medium",
    )

    description = models.TextField(blank=True)
    due_date = models.DateField(null=True, blank=True)
    estimated_minutes = models.PositiveIntegerField(default=25)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title