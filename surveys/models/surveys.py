from django.db import models
from django.conf import settings


class Survey(models.Model):
    """Store surveys."""

    name = models.CharField(max_length=250)
    fields = models.JSONField()
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        related_name='creators')

    def get_fields_default_values(self):
        fields_list = [f"{key}.{i}" for key, val in self.fields.items() for i in val]
        return {i: {j: {"value": None, "reason": ""} for j in fields_list} for i in fields_list}
