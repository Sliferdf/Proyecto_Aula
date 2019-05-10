from .viewsets import RegistroViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register('nuevos', RegistroViewSet)

urlpatterns = router.urls
