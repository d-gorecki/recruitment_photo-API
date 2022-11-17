from photo.models import Photo
from rest_framework import serializers


class PhotoCreateUpdateSerializer(serializers.ModelSerializer):
    URL = serializers.URLField(source="external_URL")

    class Meta:
        model = Photo
        fields = (
            "album_id",
            "title",
            "URL",
        )
