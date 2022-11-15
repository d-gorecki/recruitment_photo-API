from django.db.models import QuerySet
from rest_framework import viewsets
from photo.models import Photo
from API.serailizers.photo_serializer import PhotoSerializer
from API.serailizers.photo_create_update_serializer import PhotoCreateUpdateSerializer
from rest_framework import permissions
from rest_framework import serializers


class PhotosViewSet(viewsets.ModelViewSet):
    queryset: QuerySet[Photo] = Photo.objects.all()
    permission_classes: list[permissions] = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class: PhotoSerializer = PhotoSerializer
    serializer_action_classes: dict[str, serializers.ModelSerializer] = {
        "create": PhotoCreateUpdateSerializer,
        "update": PhotoCreateUpdateSerializer,
    }

    def get_serializer_class(self):
        try:
            return self.serializer_action_classes[self.action]
        except (KeyError, AttributeError):
            return super().get_serializer_class()
