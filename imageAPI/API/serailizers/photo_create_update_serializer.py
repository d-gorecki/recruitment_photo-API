from rest_framework import serializers
from photo.models import Photo
from photo.functionality import ImportPhoto


class PhotoCreateUpdateSerializer(serializers.ModelSerializer):
    URL = serializers.URLField()

    class Meta:
        model = Photo
        fields = ["album_id", "title", "URL"]

    def create(self, validated_data):
        curr_id = int(Photo.objects.last().id) + 1
        validated_data["id"] = curr_id
        img_path = ImportPhoto.download_photo(validated_data)
        record = ImportPhoto.calculate_record_data(validated_data, img_path)
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
        print(validated_data)
        validated_data["id"] = instance.id
        img_path = ImportPhoto.download_photo(validated_data)
        record = ImportPhoto.calculate_record_data(validated_data, img_path)
        instance.album_id = validated_data.get("album_id")
        instance.title = validated_data.get("title")
        instance.URL = record.get("url")
        instance.width = record.get("width")
        instance.height = record.get("height")
        instance.domaint_color = record.get("dominant_color")
        instance.save()

        return instance
