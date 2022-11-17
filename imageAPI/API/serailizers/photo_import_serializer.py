from photo.models import Photo
from rest_framework import serializers


class PhotoImportSerializer(serializers.ModelSerializer):
    albumId = serializers.IntegerField(source="album_id")
    url = serializers.URLField(source="external_URL")

    class Meta:
        model = Photo
        fields = ("id", "albumId", "title", "url")
