from django.urls import path
from .api_endpoints import FrontendTranslationView, VersionHistoryView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = "common"

urlpatterns = [
    path("FrontendTranslations/", FrontendTranslationView.as_view(), name="frontend-translations"),
    path("VersionHistory/", VersionHistoryView.as_view(), name="version-history"),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
