from rest_framework import routers
from .viewsets import SitiosViewSet
# esta clase va a definir la ruta para nuestros modelos y el put, push, delete, patch entre otros
router = routers.SimpleRouter()
router.register('sitios', SitiosViewSet)

urlpatterns = router.urls
