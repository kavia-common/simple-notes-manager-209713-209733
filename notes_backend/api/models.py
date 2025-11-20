from django.db import models


class Note(models.Model):
    """
    Note model representing a simple note with title, content, and timestamps.
    """
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)  # set on create
    updated_at = models.DateTimeField(auto_now=True)      # set on each update

    class Meta:
        ordering = ["-updated_at"]  # default ordering by latest updated

    def __str__(self) -> str:
        return f"{self.title} (#{self.pk})"
