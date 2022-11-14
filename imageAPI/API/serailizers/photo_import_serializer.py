from rest_framework import serializers
from photo.models import Photo


# using source= params raises [ErrorDetail(string='This field is required.', code='required')] for some fields


class PhotoImportSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    albumId = serializers.IntegerField()
    title = serializers.CharField(max_length=240)
    width = serializers.IntegerField()
    height = serializers.IntegerField()
    dominant_color = serializers.CharField()
    url = serializers.URLField()

    def create(self, validated_data):
        return Photo.objects.create(
            id=validated_data.get("id"),
            album_id=validated_data.get("albumId"),
            title=validated_data.get("title"),
            width=validated_data.get("width"),
            height=validated_data.get("height"),
            dominant_color=validated_data.get("dominant_color"),
            URL=validated_data.get("url"),
        )
