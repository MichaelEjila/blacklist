from rest_framework import serializers
from main.models import FlaggedData, DataType


class DataTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataType
        fields = '__all__'

class FlaggedDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlaggedData
        fields = '__all__'

