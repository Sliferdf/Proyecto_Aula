from .viewsets import UsersViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register('users', UsersViewSet)

urlpatterns = router.urls
