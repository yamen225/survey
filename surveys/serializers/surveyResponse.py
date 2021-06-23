from rest_framework import serializers
from ..models import SurveyResponse


class SurveyResponseSerializer(serializers.ModelSerializer):
    responder = serializers.CharField(source="responder__username", read_only=True)
    class Meta:
        model = SurveyResponse
        fields = ('survey', 'answers', 'responder')
