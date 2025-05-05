from django.db import models
from django.utils import timezone
from uuid import uuid4
from django.conf import settings
import os


def prompt_markdown_upload_path(instance, filename):
    # Store markdown files in PROMPT_STORAGE_DIR, filename is uuid.md
    return os.path.join(
        getattr(settings, 'PROMPT_STORAGE_DIR', 'prompts'),
        f"{instance.id}.md"
    )


class Prompt(models.Model):
    """
    Stores prompt metadata. Content is stored in a markdown file on disk.
    """
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    # Only store the relative path to the markdown file
    markdown_path = models.CharField(max_length=255, editable=False)

    class Meta:
        ordering = ['-updated_at']
        indexes = [models.Index(fields=['title'])]

    def __str__(self) -> str:
        return self.title
