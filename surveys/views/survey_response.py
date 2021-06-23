from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from ..models import SurveyResponse, Survey
from ..serializers import SurveyResponseSerializer


class SurveyResponseViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing accounts.
    """
    queryset = SurveyResponse.objects.all()
    serializer_class = SurveyResponseSerializer

    def perform_create(self, serializer):
        if self.request and hasattr(self.request, 'user'):
            self.request.data['responder'] = self.request.user
        serializer.save(responder=self.request.user)

    @action(detail=True, methods=["get"])
    def get_answers(self, request, pk=None, *args, **kwargs):
        user = request.user
        try:
            survey_answers = SurveyResponse.objects.get(survey_id=pk, responder=user).answers
        except SurveyResponse.DoesNotExist:
            print(pk)
            survey = Survey.objects.get(pk=pk)
            survey_answers = SurveyResponse.objects.create(
                survey=survey, responder=user, answers=survey.get_fields_default_values())
            survey_answers = survey_answers.answers
        return Response(survey_answers)
