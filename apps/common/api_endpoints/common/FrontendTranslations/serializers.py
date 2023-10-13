from apps.common import models
from rest_framework import serializers


class FrontendTranslationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FrontendTranslation
        fields = ("key", "text")
