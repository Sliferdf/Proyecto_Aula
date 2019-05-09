#con esta clase podemos crear un crud sobre nuestro objeto
from rest_framework import viewsets
from .models import Sitios
from .serializer import SitiosSerializer

class SitiosViewSet(viewsets.ModelViewSet):

    queryset = Sitios.objects.all()
    serializer_class = SitiosSerializer