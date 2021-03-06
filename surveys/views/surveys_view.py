from rest_framework import viewsets
from ..models import Survey
from ..serializers import SurveySerializer


class SurveyViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for viewing accounts.
    """
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer
