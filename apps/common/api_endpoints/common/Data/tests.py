import grpc
from rest_framework.test import APITestCase
from apps.common.grpc import common_pb2, common_pb2_grpc

class DataTests(APITestCase):
    def test_data(self):
        "i know this test is not safe"
        channel = grpc.insecure_channel('localhost:50051')
        stub = common_pb2_grpc.DataCreateControllerStub(channel)
        request = common_pb2.DataRequest(
            name='Test',
            description='Test',
            data_json=None
        )
        response = stub.Create(request)
        print(response)
        