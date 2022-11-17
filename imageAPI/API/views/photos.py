from API.serailizers.photo_create_update_serializer import \
    PhotoCreateUpdateSerializer
from API.serailizers.photo_serializer import PhotoSerializer
from django.db.models import QuerySet
from photo.models import Photo
from rest_framework import permissions, serializers, viewsets


class PhotosViewSet(viewsets.ModelViewSet):
    queryset: QuerySet[Photo] = Photo.objects.all()
    permission_classes: list[permissions] = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class: PhotoSerializer = PhotoSerializer
    serializer_action_classes: dict[str, serializers.ModelSerializer] = {
        "create": PhotoCreateUpdateSerializer,
        "update": PhotoCreateUpdateSerializer,
        "list": PhotoSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_action_classes.get(
            self.action, super().get_serializer_class()
        )
