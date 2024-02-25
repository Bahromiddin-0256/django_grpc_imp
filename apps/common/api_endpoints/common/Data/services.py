from django_socio_grpc import generics
from apps.common.models import Data
from .serializer import DataProtoSerializer


class DataCreateService(generics.AsyncCreateService):
    queryset = Data.objects.all()
    serializer_class = DataProtoSerializer
    

class DataListService(generics.AsyncListService):
    queryset = Data.objects.all()
    serializer_class = DataProtoSerializer
    