from .models import Data
from rest_framework import serializers

class DataModels(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = '__all__'