from .models import User
from .serializer import UsersSerializer
from rest_framework import viewsets

class UsersViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UsersSerializer
