from django.conf import settings
from ..models import Survey, SurveyResponse

class SurveyAnswer(object):
    def __init__(self, survey, *args, **kwargs):
        self.survey = Survey.objects.get(pk=survey)
        self.categories = self.survey.get_categories()
        self.fields = self.survey.get_fields()
        self.fields_values = self.survey.get_fields_values()

    def get_survey_answer(self, user: settings.AUTH_USER_MODEL, *args, **kwargs):
        try:
            SurveyResponse.objects.get(survey=self.survey, responder=user)
        except SurveyResponse.DoesNotExist:
            SurveyResponse.objects.create(
                survey=self.survey, responder=user, fields=self.survey.get_fields())
        return True
