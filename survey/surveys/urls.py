from rest_framework import routers
from .views import SurveyViewSet

router = routers.SimpleRouter()
router.register(r'', SurveyViewSet)

urlpatterns = router.urls
