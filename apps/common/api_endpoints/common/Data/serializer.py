from django_socio_grpc import proto_serializers
from rest_framework import serializers
from apps.common.models import Data
from apps.common.grpc.common_pb2 import DataListResponse, DataResponse

class DataProtoSerializer(proto_serializers.ModelProtoSerializer):
    class Meta:
        model = Data
        fields = '__all__'
        proto_class = DataResponse
        proto_class_list = DataListResponse
        