from apps.common import models
from rest_framework import serializers


class VersionHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.VersionHistory
        fields = ("version", "required")
