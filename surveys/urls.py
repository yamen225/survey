from rest_framework import routers
from .views import SurveyViewSet, SurveyResponseViewSet

router = routers.SimpleRouter()
router.register(r'response', SurveyResponseViewSet)
router.register(r'', SurveyViewSet)

urlpatterns = router.urls
