from django.db import models
from django.conf import settings


class Survey(models.Model):
    """Store surveys."""

    fields = models.JSONField()
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='creators')

