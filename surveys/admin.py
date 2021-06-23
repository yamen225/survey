from django.contrib import admin
from .models import Survey, SurveyResponse


class SurveyAdmin(admin.ModelAdmin):
    pass


admin.site.register(Survey, SurveyAdmin)


class SurveyResponseAdmin(admin.ModelAdmin):
    pass


admin.site.register(SurveyResponse, SurveyResponseAdmin)