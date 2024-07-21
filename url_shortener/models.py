import uuid

from django.db import models


class Redirect(models.Model):
    id = models.UUIDField(
        primary_key=True, unique=True, default=uuid.uuid4, editable=False
    )
    created_at = models.DateTimeField(auto_now_add=True)
    original_url = models.URLField()
    url_hash = models.CharField(max_length=8, unique=True)
    hits = models.PositiveIntegerField(help_text="Track the number of hits on this URL")
    last_hit = models.DateTimeField(null=True)
