from .models import User
from rest_framework import serializers

class UsersSerializer(serializers.ModelSerializer):
    # con que modelos trabajaremos y qué campos
    class Meta:
        model = User
        fields = '__all__'
