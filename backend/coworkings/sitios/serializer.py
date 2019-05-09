
from .models import Sitios
from rest_framework import serializers
# este permite transportar los objetos a traves de un tipo de archivo JSON u otro
class SitiosSerializer(serializers.ModelSerializer):
    # con que modelos trabajaremos y qué campos
    class Meta:
        model = Sitios
        fields = '__all__'

        