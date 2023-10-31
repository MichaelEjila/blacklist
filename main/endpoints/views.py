from main.endpoints.serializers import FlaggedDataSerializer, DataTypeSerializer
from main.models import FlaggedData, DataType
from rest_framework import viewsets, status
from rest_framework.response import Response

class DataTypeViewSet(viewsets.ModelViewSet):
    queryset = DataType.objects.all()
    serializer_class = DataTypeSerializer
    lookup_field = 'name'

class FlaggedDataViewSet(viewsets.ModelViewSet):
    queryset = FlaggedData.objects.all()
    serializer_class = FlaggedDataSerializer
    lookup_field = 'value'

    def retrieve(self, request, value=None):
        try:
            data = FlaggedData.objects.get(value=value)
        except FlaggedData.DoesNotExist:
            return Response("Flagged data not found", status=status.HTTP_404_NOT_FOUND)
        
        serializer = FlaggedDataSerializer(data)
        response_data = {
            "data": serializer.data,
            "Cartegory": data.data_type.name
        }

        return Response(response_data)
