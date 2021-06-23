from django.db import models
from django.conf import settings


class SurveyResponse(models.Model):
    """Responses on a given survey."""

    responder = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='responders')
    survey = models.ForeignKey('surveys.Survey', on_delete=models.DO_NOTHING, related_name='responses')
    answers = models.JSONField()

    class Meta:
        unique_together = ('responder', 'survey')
