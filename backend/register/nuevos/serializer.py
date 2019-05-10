from .models import Registro
from rest_framework import serializers


class RegistroSerializer(serializers.ModelSerializer):
    # con que modelos trabajaremos y qué campos
    class Meta:
        model = Registro
        fields = '__all__'
