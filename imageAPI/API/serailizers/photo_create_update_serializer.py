from typing import Any, Optional

from photo.functionality import ImportPhoto
from photo.models import Photo
from rest_framework import serializers


class PhotoCreateUpdateSerializer(serializers.ModelSerializer):
    URL = serializers.URLField()

    class Meta:
        model = Photo
        fields = ["album_id", "title", "URL"]

    def create(self, validated_data):
        curr_id: Optional[int] = Photo.objects.last().id
        # as photo path is based on record id and photo is being downloaded before creating new record
        # id has to be initialized manually
        if not curr_id:
            curr_id = 1
        else:
            curr_id += 1

        validated_data["id"]: int = curr_id
        img_path: str = ImportPhoto.download_photo(validated_data)
        record: dict[str, Any] = ImportPhoto.calculate_record_data(
            validated_data, img_path
        )
        return Photo.objects.create(
            id=record.get("id"),
            album_id=record.get("album_id"),
            title=record.get("title"),
            width=record.get("width"),
            height=record.get("height"),
            dominant_color=record.get("dominant_color"),
            URL=record.get("url"),
        )

    def update(self, instance, validated_data):
        validated_data["id"]: int = instance.id
        img_path: str = ImportPhoto.download_photo(validated_data)
        record: dict[str, Any] = ImportPhoto.calculate_record_data(
            validated_data, img_path
        )
        instance.album_id: int = validated_data.get("album_id")
        instance.title: str = validated_data.get("title")
        instance.URL: str = record.get("url")
        instance.width: int = record.get("width")
        instance.height: int = record.get("height")
        instance.dominant_color: str = record.get("dominant_color")
        instance.save()

        return instance
