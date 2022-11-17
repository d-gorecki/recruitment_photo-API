from photo.models import Photo
from rest_framework import serializers


class PhotoSerializer(serializers.ModelSerializer):
    URL = serializers.URLField()

    class Meta:
        model = Photo
        fields = (
            "id",
            "album_id",
            "title",
            "width",
            "height",
            "dominant_color",
            "URL",
        )
        read_only_fields = (
            "width",
            "height",
            "dominant_color",
        )
