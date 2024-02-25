from django_socio_grpc.services.app_handler_registry import AppHandlerRegistry
from apps.common.api_endpoints import DataCreateService, DataListService


def grpc_handlers(server):
    app_registry = AppHandlerRegistry("common", server)
    app_registry.register(DataCreateService)
    app_registry.register(DataListService)
    